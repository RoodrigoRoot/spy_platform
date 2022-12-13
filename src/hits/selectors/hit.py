from src.hits.models import Hit


def get_all_my_hits(email: str):
    return Hit.objects.get_my_hits(email)

