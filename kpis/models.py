from django.db import models

# Create your models here.
class Estudiante(models.Model):
    Genero_Hombre = 0
    Genero_Mujer = 1
    Genero = [(Genero_Hombre, 'Hombre'),(Genero_Mujer, 'Mujer')]

    id_estudiante = models.AutoField(primary_key=True)
    nombre_estudiante = models.CharField(max_length=50)
    apellido_estudiante = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    genero = models.IntegerField(choices=Genero)

    def __str__(self):
        return self.nombre_estudiante + ", "+self.apellido_estudiante
