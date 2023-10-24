from django.urls import path

from message import consumers

websocket_urlpatterns = [
    # path('ws/message/', consumers.MessageConsumer.as_asgi()),
    path('ws/message/<int:pk>/', consumers.MessageConsumer.as_asgi()),
]
