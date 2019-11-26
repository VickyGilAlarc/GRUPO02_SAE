# Generated by Django 2.2.5 on 2019-11-14 16:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20191111_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='answers_at_end',
            field=models.BooleanField(default=False, help_text='La respuesta correcta NO es mostrada despeus de la pregunta. La respuesta correcta se muesta al finalizar el quiz.', verbose_name='Respuestas al final'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Category', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='description',
            field=models.TextField(blank=True, help_text='Una pequeña descripcion de que materias seran evaluadas', verbose_name='Descripcion del quiz'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='fail_text',
            field=models.TextField(blank=True, help_text='Muestra un mensaje si el alumno no aprueba el quiz.', verbose_name='Mensaje reprobatorio'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='max_questions',
            field=models.PositiveIntegerField(blank=True, help_text='Numero de preguntas que seran respondidas en cada intento.', null=True, verbose_name='Numero maximo de preguntas'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='nivel_quizz',
            field=models.IntegerField(blank=True, choices=[(3, 'Alto'), (2, 'Medio'), (1, 'Bajo')], null=True, verbose_name='Nivel de dificultad del quiz'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='pass_mark',
            field=models.SmallIntegerField(blank=True, default=0, help_text='Porcentaje necesario para pasar el examen (1 a 100%)', validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Puntaje para pasar'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='random_order',
            field=models.BooleanField(default=False, help_text='Mostrar las preguntas en orden aleatorio o como fueron creadas?', verbose_name='Orden aleatorio'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='single_attempt',
            field=models.BooleanField(default=False, help_text='Si esta tickeado, solo se prodra realizar UNA vez el quiz', verbose_name='Solo un intento'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='success_text',
            field=models.TextField(blank=True, help_text='Muestra un mensaje si el alumno aprueba el quiz.', verbose_name='Mensaje de aprovacion'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='title',
            field=models.CharField(max_length=60, verbose_name='Nombre del quiz'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='url',
            field=models.SlugField(help_text='Url para usuarios', max_length=60, verbose_name='Url de facil acceso para el quiz'),
        ),
    ]