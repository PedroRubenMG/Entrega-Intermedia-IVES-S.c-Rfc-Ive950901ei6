"""ProyectoCoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from AppCoder.views import AgregarAlumno, Inicio, AgregarConcepto, AgregarCuenta, buscar_cuentas, buscar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agregar/',AgregarAlumno, name="Agregar"),
    path('agregar_conceptos/',AgregarConcepto, name="AgregarConceptos"),
    path('agregar_cuentas/',AgregarCuenta, name="AgregarCuentas"),
    path('buscar_cuentas/', buscar_cuentas, name="BuscarCuentas"),
    path('buscar/', buscar, name="Buscar"),
    path('', Inicio),
]
