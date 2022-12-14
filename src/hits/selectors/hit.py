from django.db.models import QuerySet

from src.hits.models import Hit


def get_all_my_hits(email: str) -> QuerySet[Hit]:
    """
    Get all hits from user regardless if it's Hitmen,
    Manager or BigBoss

    Args:
        email (str): Email from user

    Returns:
        QuerySet[Hit]: All hits of user and his subordinates
    """
    return Hit.objects.get_my_hits(email)

