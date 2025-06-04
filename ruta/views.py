
from datetime import timedelta
from django_filters.rest_framework import DjangoFilterBackend
# External imports
from rest_framework import viewsets, filters
from django.utils import timezone as tz

# Local imports
from ruta.serializers import *
from ruta.models import *


class UnidadDeMedidaViewSet(viewsets.ModelViewSet):
    queryset = UnidadDeMedida.objects.all()
    serializer_class = UnidadDeMedidaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre_completo', 'simbolo', 'tipo_unidad']


class GrupoAlimenticioViewSet(viewsets.ModelViewSet):
    queryset = GrupoAlimenticio.objects.all()
    serializer_class = GrupoAlimenticioSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'descripcion']
   
class AlimentoViewSet(viewsets.ModelViewSet):
    queryset = Alimento.objects.all()
    serializer_class = AlimentoSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend] 
    search_fields = ['nombre', 'descripcion_breve', 'fuente_datos']
    filterset_fields = ['es_procesado', 'grupo'] 


class NutrienteViewSet(viewsets.ModelViewSet):
    queryset = Nutriente.objects.all()
    serializer_class = NutrienteSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['nombre', 'descripcion']
    filterset_fields = ['es_macro', 'unidad_medida_estandar']

class ValorNutricionalViewSet(viewsets.ModelViewSet):
    queryset = ValorNutricional.objects.all()
    serializer_class = ValorNutricionalSerializer
    filter_backends = [DjangoFilterBackend] 
    filterset_fields = [
        'alimento',          
        'nutriente',         
        'unidad_medida',     
        'cantidad',         
        'cantidad_referencia', 
        'porcentaje_vd'      
    ]