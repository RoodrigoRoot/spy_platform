from django.db import models
from datetime import datetime as dt

class ModelBase(models.Model):
    """
    This models is for import in other Models and be able to have
    the created_at field default
    """
    created_at = models.DateTimeField(default=dt.now())

    class Meta:
        abstract = True
        ordering = ('-created_at', )
