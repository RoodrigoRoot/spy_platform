from typing import Dict
from django.contrib.auth.models import Group


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
