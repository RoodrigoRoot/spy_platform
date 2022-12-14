from django.core.exceptions import ValidationError

from src.hitmens.models import User


def transition(user: User, new_is_active):
    source = [
        False
    ]
    can_transition(new_is_active, source)
    user.is_active = new_is_active
    user.save()
    return user


def can_transition(is_active, source):
    if is_active == source:
        raise ValidationError(f"The current status already is: {is_active}")


