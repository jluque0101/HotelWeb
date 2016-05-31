# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 16:46
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id_habitacion', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(blank=True, max_length=200)),
                ('tipo', models.CharField(choices=[(b'Fumador', b'Fumador'), (b'NoFumador', b'No fumador')], default=b'PISO', max_length=10)),
                ('lat', models.FloatField(default=0.0, null=True)),
                ('lng', models.FloatField(default=0.0, null=True)),
                ('descripcion', models.TextField(blank=True, verbose_name=b'Descripcion')),
                ('direccion', models.CharField(blank=True, max_length=200)),
                ('fecha_registro', models.DateField(default=datetime.date.today, verbose_name=b'Fecha registro')),
                ('precio', models.FloatField(default=0.0)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id_habitacion'],
                'verbose_name_plural': 'Pisos',
            },
        ),
        migrations.RemoveField(
            model_name='piso',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='imagen',
            options={'ordering': ['id_habitacion'], 'verbose_name_plural': 'Imagenes'},
        ),
        migrations.RemoveField(
            model_name='imagen',
            name='id_piso',
        ),
        migrations.DeleteModel(
            name='Piso',
        ),
        migrations.AddField(
            model_name='imagen',
            name='id_habitacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Habitacion'),
        ),
    ]
