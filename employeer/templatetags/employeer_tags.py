from django import template
from django.contrib.auth import get_user_model


register = template.Library()

@register.filter(name='is_applied')
def is_applied(user, job):
    user = get_user_model().objects.get(id=user.id)
    if user.is_applicant:
        if user.applicant_applications.filter(job=job).exists():
            return True
    return False
