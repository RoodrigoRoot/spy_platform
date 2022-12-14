from src.hitmens.models import Hitmen, User


def create_hitmen(user: User) -> Hitmen:
    """
    This function is to create a Hitmen, after create a user

    Args:
        user (User): User object to assign a Hitmen

    Returns:
        Hitmen: Hitmen Object
    """
    hitmen = Hitmen(
        user=user,
        title=Hitmen.TitleType.HITMEN
    )
    hitmen.save()
    return hitmen



