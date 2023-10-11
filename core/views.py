from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from employeer.models import Employeer


class HomeView(TemplateView):
    template_name = 'home.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):    
    template_name = 'contact.html'
    

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'

