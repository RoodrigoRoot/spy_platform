from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name) -> bool:
    """
    This is a custom tag to use in the templates.
    With this tag we can validate if a user has it certain groups
    Args:
        user (_type_): User to check groups
        group_name (_type_): Group name to validate if the user has it

    Returns:
        bool: return a boolean response
    """
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False