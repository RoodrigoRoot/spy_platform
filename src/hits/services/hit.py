from typing import Dict

from django.core.exceptions import ValidationError

from src.hits.models import Hit
from src.hitmens.models import Hitmen

"""
This file to manage all logic bussines
Operations like Create, Update or Delete Hitmen
Or more complex related with other business rules

"""


def update_assigned_hit(hit_pk: int, new_hitmen: Hitmen) -> Hit:
    """
    With this functions we can change Hitmen as long as
    the new hitmen is active
    
    Args:
        hit_pk (int): id of hitmen to search with orm
        new_hitmen (Hitmen): New Hitmen assigned to the Hit

    Raises:
        ValidationError: If the user is not active, we can't assigned the Hit

    Returns:
        Hit: Hit object with the new Hitmen
    """
    hit: Hit = Hit.objects.get(id=hit_pk)
    if hit.assigned == new_hitmen:
        return
    if not new_hitmen.user.is_active:
        raise ValidationError("Can't not assing a deactivated user")
    hit.assigned = new_hitmen
    hit.save()
    return hit


def create_hit(data: Dict, creator: Hit) -> Hit:
    """
    Create a Hit with certain validations.
    Like i.e. We canot createa hit with a user disable

    Args:
        data (Dict): Dictionary with the data of user from a form
        creator (Hit): BigBoss or Manager

    Raises:
        ValidationError: If the Hitmen is disable raise excpetion

    Returns:
        Hit: The new Hit created
    """
    hitmen = data.pop('hitmen', '')
    hit = Hit(**data)
    if not hitmen.is_active:
        raise ValidationError("Can't not assing a deactivated user")
    hit.creator = creator
    hit.save()
    return hit
