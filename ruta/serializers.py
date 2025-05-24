from ruta.models import *
from rest_framework import serializers

class UnidadDeMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadDeMedida
        fields = [
            "simbolo",
            "nombre_completo",
            "tipo_unidad",
        ]

class GrupoAlimenticioSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoAlimenticio
        fields = "__all__"

class AlimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimento
        fields = "__all__"

class NutrienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutriente
        fields = "__all__"
    
class ValorNutricionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValorNutricional
        fields = "__all__"