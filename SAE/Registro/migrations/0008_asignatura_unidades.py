# Generated by Django 2.2.5 on 2019-11-03 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0007_auto_20191017_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignatura',
            name='unidades',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]