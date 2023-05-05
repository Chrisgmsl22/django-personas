from django.forms import ModelForm, EmailInput, TextInput

from personas.models import Persona, Domicilio


class PersonaForm(ModelForm):
    class Meta:
        # Su modelo es la clase Persona
        model = Persona
        fields = '__all__' # para incluir todos los campos del modelo
        widgets = {
            'email': EmailInput(attrs={'type': 'email'}),
        }
        exclude = []

class DomicilioForm(ModelForm):
    class Meta:
        model = Domicilio
        fields = '__all__'
        widgets = {
            'calle': TextInput(attrs={'type': 'text'}),
            'numero': TextInput(attrs={'type': 'number'}),
            'localidad': TextInput(attrs={'type': 'text'}),
        }
        exclude = []