# Generated by Django 4.0.4 on 2022-12-14 02:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hitmens', '0003_alter_hitmen_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hitmen',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 14, 2, 34, 32, 699311)),
        ),
    ]
