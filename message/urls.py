from django.urls import path

from message import views

app_name = 'message'

urlpatterns = [
    path('', views.IndexView.as_view(), name='message_list'),
    path('user/<int:pk>/', views.MessageView.as_view(), name='message_detail'),
]
