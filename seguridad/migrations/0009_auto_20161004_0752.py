# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-04 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0008_maeproyecto_cod_meta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maesistema',
            name='proyectos',
        ),
        migrations.AddField(
            model_name='maeproyecto',
            name='sistemas',
            field=models.ManyToManyField(through='seguridad.ReProyectoSistema', to='seguridad.MaeSistema'),
        ),
    ]
