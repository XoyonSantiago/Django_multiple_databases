# Generated by Django 3.1.7 on 2021-04-11 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id_estudiante', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_estudiante', models.CharField(max_length=50)),
                ('apellido_estudiante', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('genero', models.IntegerField(choices=[(0, 'Hombre'), (1, 'Mujer')])),
            ],
        ),
    ]
