from django.contrib import admin

# Register your models here.
from personas.models import Persona
from personas.models import Domicilio
admin.site.register(Persona) # se registra el modelo Persona en el admin de django
admin.site.register(Domicilio) # se registra el modelo Domicilio en el admin de django
