# Generated by Django 2.2.5 on 2019-09-14 17:24

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_actividades', models.CharField(max_length=4)),
                ('nombre', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('fechanacimiento', models.DateTimeField()),
                ('sexo', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
            managers=[
                ('alumno', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Colegio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('comuna', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=20)),
            ],
            managers=[
                ('colegios', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Maestra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut_alumno', models.CharField(max_length=10)),
                ('tipo_de_permiso', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('fechanacimiento', models.DateTimeField()),
                ('sexo', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('responsabilidad', models.BooleanField()),
                ('colegio_pertenece', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registro.Colegio')),
            ],
            managers=[
                ('profesores', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.PositiveIntegerField()),
                ('codigo_actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registro.Actividades')),
                ('rut_alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registro.Alumno')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrecurso', models.CharField(max_length=20)),
                ('codigo_curso', models.CharField(max_length=4)),
                ('colegio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registro.Colegio')),
            ],
            managers=[
                ('cursos', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_asignatura', models.CharField(max_length=20)),
                ('codigo', models.CharField(max_length=4)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registro.Curso')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registro.Profesor')),
            ],
            managers=[
                ('asignaturas', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Apoderados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('fechanacimiento', models.DateTimeField()),
                ('sexo', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('alumnos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registro.Alumno')),
            ],
            managers=[
                ('apoderados', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='alumno',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registro.Curso'),
        ),
        migrations.AddField(
            model_name='actividades',
            name='asignatura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registro.Asignatura'),
        ),
    ]
