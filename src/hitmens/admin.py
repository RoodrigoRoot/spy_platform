from django.contrib import admin

from src.hitmens.models import Hitmen, User
# Register your models here.

admin.site.register(User)
admin.site.register(Hitmen)