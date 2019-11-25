# Generated by Django 2.2.7 on 2019-11-25 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0012_nivel'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignatura',
            name='materia',
            field=models.CharField(blank=True, choices=[('leg', 'Lenguaje'), ('mat', 'Matematicas'), ('his', 'Historia'), ('fis', 'Fisica'), ('qui', 'Quimica'), ('bio', 'Biologia'), ('ing', 'Ingles')], max_length=3, null=True),
        ),
    ]