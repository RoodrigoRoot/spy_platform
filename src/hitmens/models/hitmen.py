from django.db import models

from src.base.models import ModelBase
from src.hitmens.models import User

# Create your models here.


class SubordinatesManager(models.Manager):

    def get_subordinates_all(self, email=None):
        hitmen = self.get(user__email=email)
        if not hitmen.user.groups.filter(name='BigBoss').exists():
            return self.filter(boss=hitmen)
        return self.all().exclude(pk=hitmen.pk)


class Hitmen(ModelBase):

    class TitleType(models.TextChoices):
        BOSS = 'MANAGER', 'MANAGER'
        HITMEN = 'HITMEN', 'HITMEN'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, choices=TitleType.choices)
    boss = models.ForeignKey('self', on_delete=models.DO_NOTHING, blank=True, null=True)
    objects = SubordinatesManager()

    def __str__(self) -> str:
        return self.user.email
