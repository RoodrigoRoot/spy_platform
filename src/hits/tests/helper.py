from faker import Faker
from django.contrib.auth.models import Group

from src.hitmens.services import create_user, create_hitmen
from src.hits.services import create_hit
from src.hitmens.models import Hitmen

fake = Faker()



def create_simple_hitmen():
    user = create_user({
                "email":fake.email(),
                "password":"spy123$",
                "name":fake.name()
            })
    hitmen = create_hitmen(
                user
            )
    return hitmen


def assign_manager_to_hitmen(hitmen: Hitmen, manager: Hitmen):
    hitmen.boss = manager
    hitmen.save()

def create_manager_hitmen():
    user = create_user({
                "email":fake.email(),
                "password":"spy123$",
                "name":fake.name()
            })
    hitmen = create_hitmen(
                user
            )
    group = Group.objects.get(name='Manager')
    user.groups.add(group)
    return hitmen


def create_hits_for_tests(hitmen, creator):
    hit_data = {
            "title":"Masha",
            "target":"El oso",
            "descriptions": "Acabar con el oso",
            "assigned": hitmen
    }
    hit = create_hit(hit_data, creator)
    return hit
