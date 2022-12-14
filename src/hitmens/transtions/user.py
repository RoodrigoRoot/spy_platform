from django.core.exceptions import ValidationError

from src.hitmens.models import User

"""
This file is to manage the finite state of is_active
"""


def transition(user: User, new_is_active) ->User:
    """
    Manage the is_active value to check if it's possible change value
    Args:
        user (User): The user to change
        new_is_active (bool): New value to is_active

    Returns:
        user (User): User Changed
    """
    source = [
        False
    ]
    can_transition(new_is_active, source)
    user.is_active = new_is_active
    user.save()
    return user


def can_transition(is_active, source):
    """
    This function is to validate that not assing the same status

    Args:
        is_active (bool): Current value of is_acitve
        source (List): List of not allowed status

    Raises:
        ValidationError: _description_
    """
    if is_active == source:
        raise ValidationError(f"The current status already is: {is_active}")


