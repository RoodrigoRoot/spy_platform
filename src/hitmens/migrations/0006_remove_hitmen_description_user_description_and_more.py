# Generated by Django 4.0.4 on 2022-12-14 07:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hitmens', '0005_hitmen_description_user_name_alter_hitmen_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hitmen',
            name='description',
        ),
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hitmen',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 14, 7, 20, 54, 653747)),
        ),
    ]