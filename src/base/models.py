from django.db import models


class ModelBase(models.Model):

    created_at = models.DateTimeField()

    class Meta:
        abstract = True
        ordering = ('-created_at', )
