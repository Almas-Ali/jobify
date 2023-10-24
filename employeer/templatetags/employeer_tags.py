from django import template
from django.contrib.auth import get_user_model

from job.models import Job, Application

register = template.Library()

@register.filter(name='is_applied')
def is_applied(user, job):
    user = get_user_model().objects.get(id=user.id)
    if user.is_applicant:
        if user.applicant_applications.filter(job=job).exists():
            return True
    return False


@register.filter(name='get_applicants_count')
def get_applicants_count(job_id):
    return Application.objects.filter(
        job=Job.objects.get(id=job_id)
    ).count()
