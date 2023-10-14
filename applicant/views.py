from django.views.generic.base import TemplateView
from django.contrib.auth import get_user_model
from django.shortcuts import get_list_or_404, redirect
from django.urls import reverse, reverse_lazy

from account.models import User


class ApplicantsView(TemplateView):
    template_name = "applicant/applicants_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["applicants"] = get_user_model(
        ).objects.filter(is_applicant=True)
        return context


class ApplicantSuspendView(TemplateView):
    def post(self, request, id, *args, **kwargs):
        applicant = get_user_model().objects.get(id=id)
        applicant.suspend()
        return redirect('applicant:applicants_list')


class ApplicantUnsuspendView(TemplateView):
    def post(self, request, id, *args, **kwargs):
        applicant = get_user_model().objects.get(id=id)
        applicant.unsuspend()
        return redirect('applicant:applicants_list')
