# Generated by Django 2.2.2 on 2019-06-24 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0002_remove_colegio_sigla'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='cupos',
            field=models.PositiveIntegerField(),
        ),
    ]
