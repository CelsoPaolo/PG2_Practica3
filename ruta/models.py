from django.db import models

from django.utils import timezone 

class UnidadDeMedida(models.Model):
    simbolo = models.CharField(max_length=10, unique=True, verbose_name="Símbolo")
    nombre_completo = models.CharField(max_length=50, unique=True, verbose_name="Nombre Completo")
    tipo_unidad = models.CharField(max_length=50, verbose_name="Tipo de Unidad") 


class GrupoAlimenticio(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Grupo")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")


class Alimento(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Alimento")
    descripcion_breve = models.TextField(blank=True, null=True, verbose_name="Descripción Breve")
    es_procesado = models.BooleanField(default=False, verbose_name="Es Procesado")
    fuente_datos = models.CharField(max_length=100, verbose_name="Fuente de Datos")
    grupo = models.ForeignKey(
        GrupoAlimenticio,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='alimentos', 
        verbose_name="Grupo Alimenticio"
    )



class Nutriente(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Nutriente")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    es_macro = models.BooleanField(default=False, verbose_name="Es Macronutriente")
    unidad_medida_estandar = models.ForeignKey(
        UnidadDeMedida,
        on_delete=models.PROTECT,
        related_name='nutrientes_con_unidad_estandar', 
        verbose_name="Unidad de Medida Estándar"
    )



class ValorNutricional(models.Model):
    alimento = models.ForeignKey(
        Alimento,
        on_delete=models.CASCADE,
        related_name='valores_nutricionales', 
        verbose_name="Alimento"
    )

    nutriente = models.ForeignKey(
        Nutriente,
        on_delete=models.CASCADE,
        related_name='valores_nutricionales', 
        verbose_name="Nutriente"
    )

    unidad_medida = models.ForeignKey(
        UnidadDeMedida,
        on_delete=models.PROTECT,
        related_name='valores_nutricionales_especificos', 
        verbose_name="Unidad de Medida del Valor"
    )

    cantidad = models.FloatField(verbose_name="Cantidad")
    referencia_por_cantidad = models.CharField(max_length=50, verbose_name="Referencia por Cantidad") 
    cantidad_referencia = models.FloatField(verbose_name="Cantidad de Referencia") 
    porcentaje_vd = models.FloatField(blank=True, null=True, verbose_name="% Valor Diario") 





  