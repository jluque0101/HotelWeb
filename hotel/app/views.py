# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files.storage import default_storage

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields.files import FieldFile
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.contrib import messages
from hotel.app.models import Habitacion

from .forms import SelectDayForm, SelectRoomForm, PersonalDataForm


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
        rooms = Habitacion.objects.order_by('precio').values()
        number_rooms = Habitacion.objects.latest('id_habitacion').id_habitacion
        context['room_number'] = number_rooms
        context['rooms'] = rooms
        context['userform'] = PersonalDataForm()
        return context


class GalleryPageView(TemplateView):
    template_name = 'gallery.html'

    def get_context_data(self, **kwargs):
        context = super(GalleryPageView, self).get_context_data(**kwargs)
        context['page'] = 'gallery'
        return context


class ContactPageView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactPageView, self).get_context_data(**kwargs)
        context['page'] = 'contact'
        return context

class TransportPageView(TemplateView):
    template_name = 'transport.html'

    def get_context_data(self, **kwargs):
        context = super(TransportPageView, self).get_context_data(**kwargs)
        context['page'] = 'transport'
        return context
