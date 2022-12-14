from typing import Dict

from django.core.exceptions import ValidationError

from src.hits.models import Hit
from src.hitmens.models import Hitmen

def update_assigned_hit(hit_pk: int, new_hitmen: Hitmen) -> Hit:
    hit: Hit = Hit.objects.get(id=hit_pk)
    if hit.assigned == new_hitmen:
        return
    if not new_hitmen.user.is_active:
        raise ValidationError("Can't not assing a deactivated user")
    hit.assigned = new_hitmen
    hit.save()
    return hit

def create_hit(data: Dict, creator: Hit) -> Hit:
    hitmen = data.pop('hitmen', '')
    hit = Hit(**data)
    if not hitmen.is_active:
        raise ValidationError("Can't not assing a deactivated user")
    hit.creator = creator
    hit.save()
    return hit
