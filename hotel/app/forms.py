# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from bootstrap3_datetime.widgets import DateTimePicker
from django.forms.formsets import BaseFormSet, formset_factory
from bootstrap3.tests import TestForm
from hotel.app.models import Habitacion


IMP_CHOICES = (
    ('1', 'imp 1'),
    ('2', 'imp 2'),
    ('3', 'imp 3'),
    ('4', 'imp 4'),
)

class SelectDayForm(forms.Form):
  llegada = forms.DateField(
      required=True,
      widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm"}))

  salida = forms.DateTimeField(
      required=True,
      widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm"}))

class SelectRoomForm(forms.Form):
    habitaciones = Habitacion.objects.order_by('precio').values()
    tupla = (('0', 'Seleccione una habitación'),)
    for h in habitaciones:
        tupla = tupla + ((h["id_habitacion"], h["titulo"]),)
    disponibles = forms.ChoiceField(label="Habitaciones disponibles", initial='Despliegue el menú para ver las habitaciones', choices=tupla,
        widget=forms.Select(attrs={"onChange":'ShowRoomInfo()'}
    ))

class PersonalDataForm(forms.Form):
    nombre = forms.CharField(required=True, max_length=40, initial='Introduzca aqui su nombre')
    apellidos = forms.CharField(required=True, max_length=60 , initial='Introduzca aqui sus apellidos')
    email = forms.EmailField(required=True, max_length=60, initial='email@subdominio.dominio')
    dni = forms.CharField(required=True, max_length=9, initial='12345678A')
    tarjeta = forms.EmailField(required=True, max_length=15, initial='Introduzca 15 dígitos sin separadores')
    codigo = forms.EmailField(required=True, max_length=3, initial='Introduzca los 3 dígitos de seguridad')
    expiracion = forms.EmailField(required=True, max_length=7, initial='Fecha de expiración MM/AAAA')
