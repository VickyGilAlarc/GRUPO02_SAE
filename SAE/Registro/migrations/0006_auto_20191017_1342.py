# Generated by Django 2.2.5 on 2019-10-17 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0005_puntaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puntaje',
            name='codigo_actividad',
            field=models.PositiveIntegerField(),
        ),
    ]
