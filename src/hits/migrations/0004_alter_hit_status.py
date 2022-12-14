# Generated by Django 4.0.4 on 2022-12-13 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hits', '0003_hit_status_hitmen_alter_hit_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hit',
            name='status',
            field=models.CharField(choices=[('CLOSED', 'CLOSED'), ('OPEN', 'OPEN'), ('SUCCESS', 'SUCCESS'), ('FAILED', 'FAILED')], default='OPEN', max_length=200),
        ),
    ]