from django.test import TestCase
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError

from src.hits.models import Hit
from src.hitmens.services import create_user, create_hitmen
from src.hits.services import create_hit
from src.hits.selectors import get_all_my_hits
from src.hits.tests.helper import (create_simple_hitmen, create_hits_for_tests,
                                   create_manager_hitmen, assign_manager_to_hitmen)

class HitsTest(TestCase):

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
        group_big_boss = Group.objects.get(name='BigBoss')
        self.user.groups.add(group_big_boss)

        def login(self):
            login = self.client.login(username='test@test.com', password='spy123$')


    def test_create_hist_hitmen_failed(self):
        """
        A Hitmen can not create a hits
        """
        first_hitmen = create_simple_hitmen()
        second_hitmen = create_simple_hitmen()
        second_hitmen.user.is_active=False
        second_hitmen.save()
        hit_data = {
            "title":"Masha",
            "target":"El oso",
            "descriptions": "Acabar con el oso",
            "assigned": second_hitmen
        }
        with self.assertRaisesMessage(ValidationError, str(["This user does not have permissions to this action"])):
            create_hit(hit_data, first_hitmen)

    def test_create_hist_BigBoss_failed(self):
        """
        A Manager or BigBoss can not create a hits with a disabled user
        """
        second_hitmen = create_simple_hitmen()
        second_hitmen.user.is_active=False
        second_hitmen.save()
        hit_data = {
            "title":"Masha",
            "target":"El oso",
            "descriptions": "Acabar con el oso",
            "assigned": second_hitmen
        }
        with self.assertRaisesMessage(ValidationError, str(["Can't not assing a deactivated user"])):
            create_hit(hit_data, self.hitmen)

    def test_create_hist_BigBoss_success(self):
        """
        A Manager or BigBoss can not create a hits with a disabled user
        """
        second_hitmen = create_simple_hitmen()
        hit_data = {
            "title":"Masha",
            "target":"El oso",
            "descriptions": "Acabar con el oso",
            "assigned": second_hitmen
        }
        hit = create_hit(hit_data, self.hitmen)
        self.assertIsNotNone(hit)
        self.assertEqual(
            hit.title, hit_data['title']
        )
        self.assertEqual(
            hit.target, hit_data['target']
        )
        self.assertEqual(
            hit.assigned, second_hitmen
        )
        self.assertEqual(
            hit.creator, self.hitmen
        )

    def test_list_hits_hitmen(self):
        """
            The Hitmens only can view his own Hits
            We create two hitmens and two hits, but each hitmen
            can only see a one hit
        """
        first_hitmen = create_simple_hitmen()
        firts_hit = create_hits_for_tests(first_hitmen, self.hitmen)

        second_hitmen = create_simple_hitmen()
        second_hit = create_hits_for_tests(second_hitmen, self.hitmen)

        hits = get_all_my_hits(first_hitmen.user.email)

        # All Hits on DB
        self.assertEqual(
            Hit.objects.count(), 2
        )

        # All Hits of a Hitmen
        self.assertEqual(
            hits.count(), 1
        )

    def test_list_hits_manager(self):
        """
            The Hitmens only can view his own Hits.
            The manager can view hits of subordinates
            We create two hitmens and two hits, but each hitmen
            can only see a one hit
        """
        first_hitmen = create_simple_hitmen()
        firts_hit = create_hits_for_tests(first_hitmen, self.hitmen)

        second_hitmen = create_simple_hitmen()
        second_hit = create_hits_for_tests(second_hitmen, self.hitmen)

        hits = get_all_my_hits(first_hitmen.user.email)

        # All Hits on DB
        self.assertEqual(
            Hit.objects.count(), 2
        )

        # All Hits of a Hitmen
        self.assertEqual(
            hits.count(), 1
        )

    def test_list_hits_manager(self):
        first_hitmen = create_simple_hitmen()
        firts_hit = create_hits_for_tests(first_hitmen, self.hitmen)
        second_hitmen = create_simple_hitmen()
        second_hit = create_hits_for_tests(second_hitmen, self.hitmen)
        manager = create_manager_hitmen()
        assign_manager_to_hitmen(first_hitmen, manager)

        hits = get_all_my_hits(manager.user.email)

        # All Hits on DB
        self.assertEqual(
            Hit.objects.count(), 2
        )

        # Manager only have a one subordinate
        # All Hits of a Hitmen
        self.assertEqual(
            len(hits), 1
        )
        self.assertNotEqual(
            second_hitmen.boss, manager
        )

    def test_list_hits_big_boss(self):
        first_hitmen = create_simple_hitmen()
        firts_hit = create_hits_for_tests(first_hitmen, self.hitmen)

        second_hitmen = create_simple_hitmen()
        second_hit = create_hits_for_tests(second_hitmen, self.hitmen)

        manager = create_manager_hitmen()
        assign_manager_to_hitmen(first_hitmen, manager)
        manager_hit = create_hits_for_tests(manager, self.hitmen)
                              # This user is Big Boss Group
        hits = get_all_my_hits(self.user.email)

        # All Hits on DB
        self.assertEqual(
            Hit.objects.count(), 3
        )

        # BigBos can see all Hits
        # All Hits of a Hitmen and Mananger
        self.assertEqual(
            hits.count(), 3
        )
