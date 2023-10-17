from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

from job.models import Job, Category, Location, Tag


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = Job.objects.all()
        context['categories'] = Category.objects.all()
        context['locations'] = Location.objects.all()
        context['tags'] = Tag.objects.all().order_by('-created_at')[:5]
        return context


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class JobDetailView(DetailView):
    template_name = 'job_details.html'
    model = Job
    context_object_name = 'job'


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'account/profile.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['user'] = get_user_model().objects.get(id=self.request.user.id)
    #     return context