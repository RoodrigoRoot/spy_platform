from django.test import TestCase
from src.hitmens.models import User, Hitmen
from src.hitmens.services import create_user, create_hitmen
from django.contrib.auth.models import Group


class RegisterTest(TestCase):
    
    def setUp(self) -> None:
        Group.objects.create(
            name='Hitmen'
        )
        Group.objects.create(
            name='Manager'
        )
        Group.objects.create(
            name='BigBoss'
        )
        self.user = create_user({
            "email":"test@test.com",
            "password":"spy123$",
            "name":"Test"
        })
        self.hitmen = create_hitmen(
            self.user
        )
        login = self.client.login(username='test@test.com', password='spy123$')


    def test_register_hitmen(self):
        new_hitmem = {
            "email":"superspia@spy.com",
            "password":"spy123$",
            "name":"Test"
        }
        new_user = create_user(new_hitmem)
        hitmen = create_hitmen(new_user)

        self.assertEqual(
            hitmen.title, Hitmen.TitleType.HITMEN
        )
        self.assertEqual(
            hitmen.user.email, new_hitmem['email']
        )
        self.assertEqual(
            hitmen.user.groups.last().name,
            'Hitmen'
        )
