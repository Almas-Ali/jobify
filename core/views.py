from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(TemplateView):
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):    
    template_name = 'contact.html'


class JobDetailView(DetailView):
    template_name = 'job_detail.html'
    # get single job detail

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'


