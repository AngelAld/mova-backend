from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from Avisos.Filters import AvisoFilter
from .models import Aviso, Alerta
from .serializers import (
    AvisoListaSerializer,
    AvisoDetalleSerializer,
    AlertaSerializer,
    AlertaAvisoListSerializer,
)
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated


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
    ordering_fields = [
        "fecha_actualizacion",
        "propiedad__precio_soles",
        "propiedad__precio_dolares",
    ]
    ordering = ["-fecha_actualizacion"]


class AvisoDetalle(RetrieveAPIView):
    queryset = Aviso.objects.all()
    serializer_class = AvisoDetalleSerializer
    lookup_field = "slug"


class AlertaLista(ListAPIView):
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [OrderingFilter]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.alertas.all()


class AlertaCreate(CreateAPIView):
    serializer_class = AlertaSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AvisoAlertaList(RetrieveAPIView):
    queryset = Alerta.objects.all()
    serializer_class = AlertaAvisoListSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [OrderingFilter]
    ordering_fields = [
        "fecha_creacion",
    ]
    ordering = ["-fecha_creacion"]

    def get_queryset(self):
        return self.request.user.alertas.all()
