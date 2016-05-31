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
      widget=DateTimePicker(options={"format": "YYYY-MM-DD"}))

  salida = forms.DateTimeField(
      required=False,
      widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm"}))

class SelectRoomForm(forms.Form):
    habitaciones = Habitacion.objects.order_by('precio').values()
    tupla = (('0', 'Seleccione una habitación'),)
    for h in habitaciones:
        tupla = tupla + ((h["id_habitacion"], h["titulo"]),)
    disponibles = forms.ChoiceField(label="Habitaciones disponibles", initial='Despliegue el menú para ver las habitaciones', choices=tupla,
        widget=forms.Select(attrs={"onChange":'ShowRoomInfo()'}
    ))
