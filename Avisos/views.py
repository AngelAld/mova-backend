from rest_framework.generics import ListAPIView, RetrieveAPIView

from Avisos.Filters import AvisoFilter
from .models import Aviso
from .serializers import AvisoListaSerializer, AvisoDetalleSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination


class AvisoLista(ListAPIView):
    queryset = Aviso.objects.all()
    serializer_class = AvisoListaSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    filterset_class = AvisoFilter
    search_fields = [
        "slug",
        "titulo",
        "estado__nombre",
        "descripcion",
        "tipo_operacion__nombre",
        "propiedad__tipo_antiguedad__nombre",
        "propiedad__subtipo_propiedad__nombre",
        "propiedad__caracteristicas__nombre",
    ]
    # filterset_fields = [

    # ]
    ordering_fields = ["fecha_actualizacion", "precio_soles", "precio_dolares"]


class AvisoDetalle(RetrieveAPIView):
    queryset = Aviso.objects.all()
    serializer_class = AvisoDetalleSerializer
    lookup_field = "slug"
