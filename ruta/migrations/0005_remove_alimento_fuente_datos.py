# Generated by Django 5.2 on 2025-06-04 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ruta', '0004_remove_alimento_fecha_ultima_actualizacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alimento',
            name='fuente_datos',
        ),
    ]
