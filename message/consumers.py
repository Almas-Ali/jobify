import json

from django.contrib.auth import get_user_model
from django.db.models import Q
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

from message.models import Message


class MessageConsumer(WebsocketConsumer):
    def connect(self):
        '''Connect to WebSocket'''

        current_user_id = self.scope['user']
        if current_user_id is None:
            return

        current_user_id = self.scope['user'].id
        other_user_id = self.scope['url_route']['kwargs']['pk']

        self.room_name = (
            f'{current_user_id}_{other_user_id}'
            if int(current_user_id) > int(other_user_id)
            else f'{other_user_id}_{current_user_id}'
        )
        # self.room_name = 'test'
        self.room_group_name = f'chat_{self.room_name}'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        # Accept the WebSocket connection
        self.accept()
        self.load_history()

    def disconnect(self, close_code):
        '''Disconnect from WebSocket'''
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )
        self.close()

    def load_history(self):
        '''Load message history'''
        self.receiver = get_user_model().objects.get(
            id=self.scope['url_route']['kwargs']['pk'])

        messages = Message.objects.filter(
            # Q(sender=self.scope['user']) | Q(receiver=self.scope['user'])
            Q(sender=self.scope['user'], receiver=self.receiver) |
            Q(sender=self.receiver, receiver=self.scope['user'])
        ).order_by('created_at')

        message_history = [
            {
                'message': message.message,
                'timestamp': message.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                'sender': message.sender.get_full_name(),
                'receiver': message.receiver.get_full_name(),
            } for message in messages
        ]

        async_to_sync(self.send(text_data=json.dumps({
            'messages': message_history,
        })))

    def receive(self, text_data):
        '''Receive message from WebSocket'''
        text_data_json = json.loads(text_data)

        message = text_data_json.get('message')

        if message is None:
            return

        # Get the sender and receiver users
        sender = self.scope['user']
        receiver = get_user_model().objects.get(
            id=self.scope['url_route']['kwargs']['pk'])

        # Create the message in the database
        message_obj = Message.objects.create(
            sender=sender,
            receiver=receiver,
            message=message
        )

        # Send the message to the receiver (if they are connected)
        self.send_message_to_receiver(message_obj)


    def send_message_to_receiver(self, message_obj):
        '''Send message to the receiver if they are connected'''

        # Construct a message to be sent
        message_data = {
            'type': 'chat.message',
            'message': message_obj.message,
            'timestamp': message_obj.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            'sender': message_obj.sender.get_full_name(),
            'sender_id': message_obj.sender.id,
            'receiver': message_obj.receiver.get_full_name(),
            'receiver_id': message_obj.receiver.id,
        }

        # Send message to WebSocket
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            message_data
        )

    def chat_message(self, event):
        '''Receive message from the WebSocket'''

        # Receive the message data from another user's WebSocket
        message = event['message']
        timestamp = event['timestamp']
        sender = event['sender']
        receiver = event['receiver']

        # Send the message to the WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'timestamp': timestamp,
            'sender': sender,
            'receiver': receiver
        }))
