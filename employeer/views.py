from django.views.generic import CreateView, ListView
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from job.models import Company, Job, Location, Tag
from employeer.forms import CompanyForm, JobForm, LocationForm, TagForm


class CreateCompanyView(LoginRequiredMixin, CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'employeer/company_create.html'
    success_url = '/employeer/'

    def post(self, request, *args, **kwargs):
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employeer:create_company')
        else:
            return render(request, 'employeer/company_create.html', {'form': form})


class CompaniesView(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'employeer/companies.html'
    context_object_name = 'companies'

    def get_queryset(self):
        return Company.objects.filter(user=self.request.user)


class JobsView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'employeer/jobs.html'
    context_object_name = 'companies'

    def get_queryset(self):
        return Job.objects.filter(user=self.request.user)


class AddJobView(LoginRequiredMixin, CreateView):
    model = Job
    form_class = JobForm
    template_name = 'employeer/add_job.html'
    success_url = '/employeer/'

    def post(self, request, *args, **kwargs):
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employeer:add_job')
        else:
            return render(request, 'employeer/add_job.html', {'form': form})


class LocationsView(LoginRequiredMixin, TemplateView):
    model = Location
    template_name = 'employeer/locations.html'
    context_object_name = 'locations'

    def get_queryset(self):
        return Location.objects.all()

    def post(self, request, *args, **kwargs):
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employeer:locations')
        else:
            return render(request, 'employeer/locations.html', {'form': form})

    def get(self, request, *args, **kwargs):
        return render(request, 'employeer/locations.html', {
            'form': LocationForm(),
            'locations': Location.objects.all()
        })


class TagsView(LoginRequiredMixin, TemplateView):
    model = Tag
    template_name = 'employeer/tags.html'
    context_object_name = 'tags'

    def get_queryset(self):
        return Tag.objects.all()

    def post(self, request, *args, **kwargs):
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employeer:tags')
        else:
            return render(request, 'employeer/tags.html', {'form': form})

    def get(self, request, *args, **kwargs):
        return render(request, 'employeer/tags.html', {
            'form': TagForm(),
            'tags': Tag.objects.all()
        })
