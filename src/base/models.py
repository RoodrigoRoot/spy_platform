from django.db import models
from datetime import datetime as dt
from django.utils.timezone import now

class ModelBase(models.Model):
    """
    This models is for import in other Models and be able to have
    the created_at field default
    """
    created_at = models.DateTimeField(default=now)

    class Meta:
        abstract = True
        ordering = ('-created_at', )
