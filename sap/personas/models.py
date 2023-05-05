from django.db import models
# Primero se definen las clases que no tienen dependencias
class Domicilio(models.Model):
    calle = models.CharField(max_length=255)
    numero = models.IntegerField() # No se define el tamaño porque es un entero
    localidad = models.CharField(max_length=255)

    def __str__(self):
        return f'Domicilio: {self.id} - {self.calle} {self.numero} {self.localidad}'



# Create your models here.
class Persona(models.Model): # models.Model es requerido
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True) # Se define la relación con el modelo Domicilio

    def __str__(self):
        return f'Persona: {self.id} - {self.nombre} {self.apellido}'
