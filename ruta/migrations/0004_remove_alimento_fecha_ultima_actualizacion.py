# Generated by Django 5.2 on 2025-06-02 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ruta', '0003_remove_alimento_imagen_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alimento',
            name='fecha_ultima_actualizacion',
        ),
    ]
