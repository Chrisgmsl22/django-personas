from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from personas.forms import PersonaForm, DomicilioForm
from personas.models import Persona, Domicilio


def detalle_persona(request, id):
    # persona_encontrada = Persona.objects.get(pk=id)
    persona_encontrada = get_object_or_404(Persona, pk=id) # si no encuentra el objeto, devuelve un 404
    return render(request, 'personas/detalle.html', {'persona': persona_encontrada})


def nueva_persona(request):
    # Si es una peticion POST, procesamos los datos del formulario
    if request.method == 'POST':
        # En request.POST se encuentran los datos del formulario
        formaPersona = PersonaForm(request.POST)
        # Validamos los datos del formulario
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')

    else:
        # Si es una peticion GET, mostramos el formulario para ingresar los datos
        # Creamos un nuevo objeto de tipo persona
        formaPersona = PersonaForm()

    return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})

def editar_persona(request, id):
    # Recuperamos la persona a editar (el objeto persona)
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        # En request.POST se encuentran los datos del formulario
        formaPersona = PersonaForm(request.POST, instance=persona)
        # Validamos los datos del formulario
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')

    else:
        # Si es una peticion GET, mostramos el formulario para ingresar los datos
        # cargamos los datos de la persona a editar, a traves del parametro instance
        formaPersona = PersonaForm(instance=persona)

    return render(request, 'personas/editar.html', {'formaPersona': formaPersona})

def eliminar_persona(request, id):
    # Recuperamos la persona a eliminar (el objeto persona)
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect('index')




# Ahora con los domicilios
def nuevo_domicilio(request):
    # Si es una peticion POST, procesamos los datos del formulario
    if request.method == 'POST':
        # En request.POST se encuentran los datos del formulario
        formaDomicilio = DomicilioForm(request.POST)
        # Validamos los datos del formulario
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('domicilios')

    else:
        # Si es una peticion GET, mostramos el formulario para ingresar los datos
        # Creamos un nuevo objeto de tipo persona
        formaDomicilio = DomicilioForm()

    return render(request, 'domicilios/nuevo.html', {'formaDomicilio': formaDomicilio})

def detalle_domicilio(request, id):
    # persona_encontrada = Persona.objects.get(pk=id)
    domicilio_encontrado = get_object_or_404(Domicilio, pk=id) # si no encuentra el objeto, devuelve un 404
    return render(request, 'domicilios/detalle.html', {'domicilio': domicilio_encontrado})

def editar_domicilio(request, id):
    # Recuperamos el domicilio a editar (el objeto persona)
    domicilio = get_object_or_404(Domicilio, pk=id)
    if request.method == 'POST':
        # En request.POST se encuentran los datos del formulario
        formaDomicilio = DomicilioForm(request.POST, instance=domicilio)
        # Validamos los datos del formulario
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('domicilios')

    else:
        # Si es una peticion GET, mostramos el formulario para ingresar los datos
        # cargamos los datos de la persona a editar, a traves del parametro instance
        formaDomicilio = DomicilioForm(instance=domicilio)

    return render(request, 'domicilios/editar.html', {'formaDomicilio': formaDomicilio})


def eliminar_domicilio(request, id):
    # Recuperamos el domicilio a eliminar (el objeto persona)
    domicilio = get_object_or_404(Domicilio, pk=id)
    if domicilio:
        domicilio.delete()
    return redirect('domicilios')