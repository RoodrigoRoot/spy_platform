from typing import List

from django.core.exceptions import ValidationError

from src.hits.models import Hit



def transition(process: Hit, destination: str):

    status_transition = {
        'COMPLETED': mark_as_completed,
        'FAILED': mark_as_failed,
    }
    process_transition = status_transition.get(process.status)
    process_transition(process, destination)
    process.status=destination
    process.save()


def mark_as_completed(process: Hit, destination: str):
    source = [
        'FAILED',
        'ASSIGNED'
    ]
    can_transition(process.status, source, destination)


def mark_as_failed(process: Hit, destination: str):
    source = [
        'COMPLETED',
        'ASSIGNED'
    ]
    can_transition(process.status, source, destination)

def can_transition(status: str, source: List[str], destination):

    if destination in source:
        raise ValidationError(f"Can't change status {status} to {destination}")

