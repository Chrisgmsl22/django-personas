from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from personas.models import Persona, Domicilio


def bienvenido(request):
    #return HttpResponse("Bienvenido a la página de inicio de SAP")
    # Usamos la clase de modelo de persona
    no_personas = Persona.objects.count()
    # personas = Persona.objects.all() # Recuperamos todos los registros de la tabla Persona
    personas = Persona.objects.order_by('id') # Recuperamos todos los registros de la tabla Persona ordenados por id

    # El metodo render puede recibir un diccionario con los datos que se quieren pasar al template
    return render(request, 'bienvenido.html', {'no_personas':no_personas, 'personas': personas}) # este metodo renderiza el template


def domicilios(request):
    domicilios_count = Domicilio.objects.count()
    domicilios = Domicilio.objects.order_by('id')

    return render(request, '../../personas/templates/domicilios/domicilios.html', {'domicilios_count': domicilios_count, 'domicilios': domicilios})