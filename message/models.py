from django.db import models
from django.contrib.auth import get_user_model

from core.models import BaseModel


class Message(BaseModel):
    # One sender can have multiple messages and one message can have only one sender
    sender = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='sender_messages')
    # One receiver can have multiple messages and one message can have only one receiver
    receiver = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='receiver_messages')
    message = models.TextField(
        max_length=1000, default='')  # Message to employer

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return self.message

    # def get_absolute_url(self):
    #     return reverse('core:job_detail', kwargs={'slug': self.slug})
