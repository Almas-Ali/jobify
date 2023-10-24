from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

from job.models import Job, Category, Location, Tag, Application
from employeer.forms import ApplicationForm


def get_matches_persenatge(job, applicant):
    '''Get the percentage of matches between a job and an applicant'''
    job_skills = job.skills.all()
    applicant_skills = applicant.skills.all()
    matches = 0
    for skill in job_skills:
        if skill in applicant_skills:
            matches += 1
    try:
        return matches / len(job_skills) * 100
    except Exception as e:
        return 0


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['jobs'] = Job.objects.filter(
                is_approved=True,
            ).exclude(
                is_closed=True
            )
        else:
            context['jobs'] = Job.objects.filter(
                is_approved=True
            )

        context['categories'] = Category.objects.all()
        context['locations'] = Location.objects.all()
        context['tags'] = Tag.objects.all().order_by('-created_at')

        if self.request.user.is_authenticated and \
                self.request.user.is_applicant:
            for job in context['jobs']:
                job.matches = get_matches_persenatge(job, self.request.user)
        else:
            context['matches'] = 0

        return context


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'

    def post(self, *args, **kwargs):
        context = {}
        context['name'] = self.request.POST.get('name')
        context['email'] = self.request.POST.get('email')
        context['subject'] = self.request.POST.get('subject')
        context['message'] = self.request.POST.get('message')
        messages.success(
            self.request, 'Your message has been sent successfully')

        return render(self.request, self.template_name, context)


class SearchView(TemplateView):
    template_name = 'search.html'

    def get(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.GET.get('category') != 'all' or \
                self.request.GET.get('location') != 'all':
            context['jobs'] = Job.objects.filter(
                Q(title__icontains=self.request.GET.get('q')) |
                Q(short_description__icontains=self.request.GET.get('q')) |
                Q(description__icontains=self.request.GET.get('q')) |
                Q(company__name__icontains=self.request.GET.get('q')) |
                Q(salary__icontains=self.request.GET.get('q')) |
                Q(category__name__icontains=self.request.GET.get('category')) |
                Q(location__name__icontains=self.request.GET.get('location')) |
                Q(tags__name__icontains=self.request.GET.get('q'))
            ).exclude(
                Q(is_closed=True) | Q(is_approved=False)
            ).distinct()

        else:
            context['jobs'] = Job.objects.filter(
                Q(title__icontains=self.request.GET.get('q')) |
                Q(short_description__icontains=self.request.GET.get('q')) |
                Q(description__icontains=self.request.GET.get('q')) |
                Q(company__name__icontains=self.request.GET.get('q')) |
                Q(salary__icontains=self.request.GET.get('q')) |
                Q(category__name__icontains=self.request.GET.get('q')) |
                Q(location__name__icontains=self.request.GET.get('q')) |
                Q(tags__name__icontains=self.request.GET.get('q'))
            ).exclude(
                Q(is_closed=True) | Q(is_approved=False)
            ).distinct()

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

        if self.request.user.is_authenticated and \
                self.request.user.is_applicant:
            for job in context['jobs']:
                job.matches = get_matches_persenatge(job, self.request.user)
        else:
            context['matches'] = 0

        # context['categories'] = Category.objects.all()[:5]
        # context['locations'] = Location.objects.all()[:5]
        # context['tags'] = Tag.objects.all().order_by('-created_at')[:5]

        # context['categories'] = context['jobs'].category.all()
        # context['locations'] = context['jobs'].location.all()
        # context['tags'] = context['jobs'].tags.all().order_by('-created_at')

        context['categories'] = []
        context['locations'] = []
        context['tags'] = []
        context['salaries'] = []

        for job in context['jobs']:
            context['categories'].append(job.category)
            context['locations'].append(job.location)
            context['tags'].append(job.tags.all())
            context['salaries'].append(job.salary)

        context['search'] = {
            'query': self.request.GET.get('q'),
            'count': context['jobs'].paginator.count,
        }

        return render(self.request, self.template_name, context)


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

        if self.request.user.is_authenticated and \
                self.request.user.is_applicant:
            context['matches'] = get_matches_persenatge(
                context['job'], self.request.user
            )
        else:
            context['matches'] = 0

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

        try:
            context['is_applied'] = Application.objects.filter(
                job=context['job'],
                applicant=self.request.user
            ).exists()
            messages.success(
                self.request, 'You have successfully applied for this job')
        except Exception as e:
            context['is_applied'] = False

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

        try:
            context['is_applied'] = Application.objects.get(
                job=context['job'],
                applicant=self.request.user
            )
            messages.success(
                self.request, 'You have already applied for this job')
            return redirect('core:apply', slug=context['job'].slug)
        except Exception as e:
            context['is_applied'] = False

        if context['form'].is_valid():
            context['form'].instance.job = context['job']
            context['form'].instance.applicant = self.request.user
            context['form'].save()
            messages.success(
                self.request, 'You have successfully applied for this job')
            return redirect('core:apply', slug=context['job'].slug)

        return render(self.request, self.template_name, context)


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'account/profile.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['user'] = get_user_model().objects.get(id=self.request.user.id)
    #     return context
