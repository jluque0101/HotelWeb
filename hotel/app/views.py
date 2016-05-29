# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files.storage import default_storage

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields.files import FieldFile
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.contrib import messages

from .forms import SelectDayForm, SelectRoomForm


# http://yuji.wordpress.com/2013/01/30/django-form-field-in-initial-data-requires-a-fieldfile-instance/
class FakeField(object):
    storage = default_storage


fieldfile = FieldFile(None, FakeField, 'dummy.txt')


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # messages.info(self.request, 'hello http://example.com')
        context['page'] = 'home'
        return context

class BookingPageView(TemplateView):
    template_name = 'booking.html'

    def get_context_data(self, **kwargs):
        context = super(BookingPageView, self).get_context_data(**kwargs)
        context['page'] = 'booking'
        context['dayform'] = SelectDayForm()
        context['roomform'] = SelectRoomForm()
        return context
