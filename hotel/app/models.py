import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Habitacion (models.Model):
	OPCIONES_CHOICES = (
		('Fumador', 'Fumador'),
		('NoFumador', 'No fumador')
	)
	id_habitacion = models.AutoField(primary_key=True)
	titulo = models.CharField (max_length=200, default='Doble')
	tipo = models.CharField(max_length=10, choices=OPCIONES_CHOICES, default="NoFumador")
	descripcion = models.TextField ('Descripcion', blank=True)

	precio = models.FloatField(default=0.0)
	planta = models.FloatField(default=0.0)
	camas = models.FloatField(default=0.0)

	REQUIRED_FIELDS = ['tipo,camas,precio,planta,descripcion']

	class Meta:
		verbose_name_plural = 'Habitaciones'
		ordering = ['id_habitacion']
	def __unicode__(self):
		return u"%s" % self.titulo

def get_img_url(instance, filename):
	return 'habitaciones/%d/%s' % (instance.id_habitacion.id_habitacion, filename)

class Imagen(models.Model):
	id_img = models.AutoField(primary_key=True)
	titulo = models.CharField (max_length=200, default='Titulo de la Imagen')
	id_habitacion = models.ForeignKey(Habitacion, blank=True, null=True)
	pic = models.ImageField(upload_to=get_img_url)
	class Meta:
		verbose_name_plural = 'Imagenes'
		ordering = ['id_habitacion']
	def __unicode__(self):
		return u"%s" % self.titulo
