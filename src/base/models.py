from django.db import models
from datetime import datetime as dt

class ModelBase(models.Model):

    created_at = models.DateTimeField(default=dt.now())

    class Meta:
        abstract = True
        ordering = ('-created_at', )
