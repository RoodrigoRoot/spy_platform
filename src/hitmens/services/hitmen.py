from src.hitmens.models import Hitmen, User


def create_hitmen(user: User) -> Hitmen:
    hitmen = Hitmen(
        user=user
    )
    hitmen.save()
    return hitmen



