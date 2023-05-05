"""
URL configuration for sap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from personas.views import detalle_persona, nueva_persona, editar_persona, eliminar_persona, nuevo_domicilio, \
    detalle_domicilio, editar_domicilio, eliminar_domicilio
from webapp.views import bienvenido, domicilios

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('bienvenido/', bienvenido),
    path('', bienvenido, name='index'),
    path('detalle_persona/<int:id>', detalle_persona),
    path('nueva_persona', nueva_persona),
    path('editar_persona/<int:id>', editar_persona),
    path('eliminar_persona/<int:id>', eliminar_persona),
    # Ahora un path para el domicilio
    path('domicilios', domicilios, name='domicilios'),
    path('nuevo_domicilio', nuevo_domicilio),
    path('detalle_domicilio/<int:id>', detalle_domicilio),
    path('editar_domicilio/<int:id>', editar_domicilio),
    path('eliminar_domicilio/<int:id>', eliminar_domicilio)

]
