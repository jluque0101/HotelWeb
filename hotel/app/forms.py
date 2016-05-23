# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from bootstrap3_datetime.widgets import DateTimePicker
from django.forms.formsets import BaseFormSet, formset_factory
from bootstrap3.tests import TestForm


class ToDoForm(forms.Form):
  llegada = forms.DateField(
      widget=DateTimePicker(options={"format": "YYYY-MM-DD"}))

  salida = forms.DateTimeField(
      required=False,
      widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm"}))
