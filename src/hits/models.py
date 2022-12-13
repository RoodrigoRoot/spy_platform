from itertools import chain

from django.db import models
from src.hitmens.models import Hitmen

from src.base.models import ModelBase
from src.hitmens.models import Hitmen
# Create your models here.


class MyHits(models.Manager):

    def get_my_hits(self, email):
        hitmen = Hitmen.objects.get(user__email=email)
        if hitmen.user.groups.filter(name='BigBoss').exists():
            return self.all().order_by('-created_at')
        elif hitmen.user.groups.filter(name='Manager').exists():
            manager_hits = self.filter(models.Q(assigned=hitmen) | models.Q(creator=hitmen)).order_by('-created_at')
            lackey_hits = self.get_lackey_hits(email)
            if lackey_hits:
                manager_hits  = list(chain(manager_hits, lackey_hits))
            return manager_hits
        else:
            return self.filter(assigned=hitmen).order_by('-created_at')

    def get_lackey_hits(self, email):
        subordinates = Hitmen.objects.get_subordinates_all(email)
        hits = []
        for subodinate in subordinates:
            hits += self.filter(assigned=subodinate).order_by('-created_at')
        return hits


class Hit(ModelBase):

    class StatusHit(models.TextChoices):
        ASSIGNED = 'ASSIGNED', 'ASSIGNED'
        COMPLETED = 'COMPLETED', 'COMPLETED'
        FAILED_ASSIGNED = 'FAILED_ASSIGNED', 'FAILED_ASSIGNED'
        FAILED = 'FAILED', 'FAILED'

    title = models.CharField(max_length=200)
    target = models.CharField(max_length=200)
    descriptions = models.TextField()
    creator = models.ForeignKey(Hitmen, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=200, choices=StatusHit.choices, default=StatusHit.ASSIGNED)
    assigned = models.ForeignKey(Hitmen, on_delete=models.DO_NOTHING, related_name='hits')
    objects = MyHits()

