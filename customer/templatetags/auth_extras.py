from django import template
from django.contrib.auth.models import Group


register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    user_groups = user.groups.all()
    if group in user_groups:
        return True
    else:
        return False

