from typing import Dict
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError

from src.hitmens.transtions.user import transition
from src.hitmens.models import User


def create_user(data: Dict) -> User:
    """
    This function create a record user
    Args:
        Data: Is a dictionary
        {
            "email": "rod@spy.com",
            "password": "Rod123&
        }
    Return:
        A User object
    """
    password = data.pop('password')
    user = User(**data)
    user.set_password(password)
    user.is_active = True
    user.save()
    hitmen_group = Group.objects.get(name='Hitmen')
    hitmen_group.user_set.add(user)
    return user

def change_active_user(user: User, user_authorization: User, new_status: bool) -> User:
    """
    We validate if user has permissions to disable a user.
    The permission required is to belong to the group of Manager or BigBoss
    Args:
        user (User): User to disable
        user_authorization (User): authorizing user
        new_status (bool): The new status to user (True or False)

    Raises:
        ValidationError: If the user does not have permissions to change is_active of other users

    Returns:
        User: User with a new status of is_active
    """
    if not user_authorization.groups.filter(name__in=['BigBoss', 'Manager']).exists():
        raise ValidationError('This user does not have permissions to this action')
    transition(user, new_status)
    return user