
from datetime import timedelta

# External imports
from rest_framework import viewsets
from django.utils import timezone as tz

# Local imports
from ruta.serializers import *
from ruta.models import *


class UnidadDeMedidaViewSet(viewsets.ModelViewSet):
    queryset = UnidadDeMedida.objects.all()
    serializer_class = UnidadDeMedidaSerializer


class GrupoAlimenticioViewSet(viewsets.ModelViewSet):
    queryset = GrupoAlimenticio.objects.all()
    serializer_class = GrupoAlimenticioSerializer
   
class AlimentoViewSet(viewsets.ModelViewSet):
    queryset = Alimento.objects.all()
    serializer_class = AlimentoSerializer


class NutrienteViewSet(viewsets.ModelViewSet):
    queryset = Nutriente.objects.all()
    serializer_class = NutrienteSerializer

class ValorNutricionalViewSet(viewsets.ModelViewSet):
    queryset = ValorNutricional.objects.all()
    serializer_class = ValorNutricionalSerializer