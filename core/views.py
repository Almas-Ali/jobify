from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.contrib import messages

from job.models import Job, Category, Location, Tag, Application
from employeer.forms import ApplicationForm


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = Job.objects.all()[0:5]
        context['categories'] = Category.objects.all()[:5]
        context['locations'] = Location.objects.all()[:5]
        context['tags'] = Tag.objects.all().order_by('-created_at')[:5]
        return context


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class SearchView(TemplateView):
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = Job.objects.filter(
            Q(title__icontains=self.request.GET.get('q')) |
            Q(short_description__icontains=self.request.GET.get('q')) |
            Q(description__icontains=self.request.GET.get('q'))
        )

        context['jobs'] = Paginator(context['jobs'], 10)
        if self.request.GET.get('page'):
            page = self.request.GET.get('page')
        else:
            page = 1

        try:
            context['jobs'] = context['jobs'].page(page)
        except PageNotAnInteger:
            context['jobs'] = context['jobs'].page(1)
        except EmptyPage:
            context['jobs'] = context['jobs'].page(context['jobs'].num_pages)

        context['categories'] = Category.objects.all()[:5]
        context['locations'] = Location.objects.all()[:5]
        context['tags'] = Tag.objects.all().order_by('-created_at')[:5]
        return context


class JobDetailView(TemplateView):
    template_name = 'job_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job'] = Job.objects.get(slug=self.kwargs['slug'])
        context['job'].views += 1
        context['job'].save()
        context['locations'] = Location.objects.all().order_by(
            '-created_at')[:5]
        context['tags'] = Tag.objects.all().order_by('-created_at')[:5]
        context['categories'] = Category.objects.all().order_by(
            '-created_at')[:5]
        return context


class ApplyView(TemplateView):
    template_name = 'apply.html'

    def get(self, *args, **kwargs):
        context = {}
        context['job'] = Job.objects.get(slug=self.kwargs['slug'])
        context['locations'] = Location.objects.all().order_by(
            '-created_at')[:5]
        context['tags'] = Tag.objects.all().order_by('-created_at')[:5]
        context['categories'] = Category.objects.all().order_by(
            '-created_at')[:5]
        context['form'] = ApplicationForm()

        context['is_applied'] = Application.objects.get(
            job=context['job'],
            applicant=self.request.user
        )

        messages.success(self.request, 'You have successfully applied for this job')
        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):
        context = {}
        context['job'] = Job.objects.get(slug=self.kwargs['slug'])
        context['locations'] = Location.objects.all().order_by(
            '-created_at')[:5]
        context['tags'] = Tag.objects.all().order_by('-created_at')[:5]
        context['categories'] = Category.objects.all().order_by(
            '-created_at')[:5]
        context['form'] = ApplicationForm(
            self.request.POST, self.request.FILES)

        context['is_applied'] = Application.objects.get(
            job=context['job'],
            applicant=self.request.user
        )

        if context['form'].is_valid():
            context['form'].instance.job = context['job']
            context['form'].instance.applicant = self.request.user
            context['form'].save()
            context['success'] = True

        return render(self.request, self.template_name, context)


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'account/profile.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['user'] = get_user_model().objects.get(id=self.request.user.id)
    #     return context
