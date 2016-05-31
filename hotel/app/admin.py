from django.contrib import admin

# Register your models here.

from hotel.app.models import Habitacion, Imagen

admin.site.register(Habitacion)
admin.site.register(Imagen)
