from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, get_list_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages

from job.models import Application


class ApplicantsView(LoginRequiredMixin, TemplateView):
    template_name = "applicant/applicants_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["applicants"] = get_user_model(
        ).objects.filter(is_applicant=True)
        return context


class ApplicantSuspendView(LoginRequiredMixin, TemplateView):
    def post(self, request, id, *args, **kwargs):
        applicant = get_user_model().objects.get(id=id)
        applicant.suspend()
        return redirect('applicant:applicants_list')


class ApplicantUnsuspendView(LoginRequiredMixin, TemplateView):
    def post(self, request, id, *args, **kwargs):
        applicant = get_user_model().objects.get(id=id)
        applicant.unsuspend()
        return redirect('applicant:applicants_list')


class SentApplicationsView(LoginRequiredMixin, TemplateView):
    template_name = "applicant/sent_applications.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["applications"] = get_list_or_404(
            Application, applicant=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        application = get_object_or_404(
            Application, applicant=self.request.user, id=request.POST.get('id')
        )
        application.delete()
        messages.success(request, 'Application deleted successfully.')
        return redirect('applicant:sent_applications')
