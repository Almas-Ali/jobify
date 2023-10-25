from django import template

from django.contrib.auth import get_user_model

register = template.Library()


@register.filter(name='get_user_full_name')
def get_user_full_name(user_id):
    user = get_user_model().objects.get(id=user_id)
    return user.get_full_name()
