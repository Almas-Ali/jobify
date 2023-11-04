from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.db.models import Q

from message.models import Message


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/messages_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = Message.objects.all()
        context['users'] = get_user_model().objects.all()
        return context


class MessageView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/message.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = Message.objects.filter(
            Q(sender=self.request.user) | Q(receiver=self.request.user) |
            Q(sender=self.kwargs['pk']) | Q(receiver=self.kwargs['pk'])
        )
        context['receiver'] = get_user_model().objects.get(id=self.kwargs['pk'])
        context['sender'] = self.request.user
        return context

    def get_queryset(self):
        return Message.objects.all()
