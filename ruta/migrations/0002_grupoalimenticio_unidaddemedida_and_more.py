# Generated by Django 5.2 on 2025-05-23 15:25

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrupoAlimenticio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre del Grupo')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='UnidadDeMedida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('simbolo', models.CharField(max_length=10, unique=True, verbose_name='Símbolo')),
                ('nombre_completo', models.CharField(max_length=50, unique=True, verbose_name='Nombre Completo')),
                ('tipo_unidad', models.CharField(max_length=50, verbose_name='Tipo de Unidad')),
            ],
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='grupos',
        ),
        migrations.RemoveField(
            model_name='punto_interes',
            name='ruta',
        ),
        migrations.RemoveField(
            model_name='rutas',
            name='usuarios',
        ),
        migrations.CreateModel(
            name='Alimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre del Alimento')),
                ('descripcion_breve', models.TextField(blank=True, null=True, verbose_name='Descripción Breve')),
                ('imagen_url', models.URLField(blank=True, null=True, verbose_name='URL de Imagen')),
                ('es_procesado', models.BooleanField(default=False, verbose_name='Es Procesado')),
                ('fuente_datos', models.CharField(max_length=100, verbose_name='Fuente de Datos')),
                ('fecha_ultima_actualizacion', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha Última Actualización')),
                ('grupo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alimentos', to='ruta.grupoalimenticio', verbose_name='Grupo Alimenticio')),
            ],
        ),
        migrations.CreateModel(
            name='Nutriente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre del Nutriente')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('es_macro', models.BooleanField(default=False, verbose_name='Es Macronutriente')),
                ('unidad_medida_estandar', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='nutrientes_con_unidad_estandar', to='ruta.unidaddemedida', verbose_name='Unidad de Medida Estándar')),
            ],
        ),
        migrations.CreateModel(
            name='ValorNutricional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.FloatField(verbose_name='Cantidad')),
                ('referencia_por_cantidad', models.CharField(max_length=50, verbose_name='Referencia por Cantidad')),
                ('cantidad_referencia', models.FloatField(verbose_name='Cantidad de Referencia')),
                ('porcentaje_vd', models.FloatField(blank=True, null=True, verbose_name='% Valor Diario')),
                ('alimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='valores_nutricionales', to='ruta.alimento', verbose_name='Alimento')),
                ('nutriente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='valores_nutricionales', to='ruta.nutriente', verbose_name='Nutriente')),
                ('unidad_medida', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='valores_nutricionales_especificos', to='ruta.unidaddemedida', verbose_name='Unidad de Medida del Valor')),
            ],
        ),
        migrations.DeleteModel(
            name='grupo',
        ),
        migrations.DeleteModel(
            name='punto_interes',
        ),
        migrations.DeleteModel(
            name='rutas',
        ),
        migrations.DeleteModel(
            name='usuario',
        ),
    ]
