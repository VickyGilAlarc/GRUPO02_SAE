# Generated by Django 2.2.5 on 2019-11-03 03:52

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0009_unidad'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='unidad',
            managers=[
                ('unidades', django.db.models.manager.Manager()),
            ],
        ),
    ]
