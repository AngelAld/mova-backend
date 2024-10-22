from .serializers import (
    PropiedadTiposSerializer,
    PropiedadListSerializer,
    TipoPropiedadSerializer,
    SubTipoPropiedadSerializer,
    TipoOperacionSerializer,
    PropiedadDatosSerializer,
    CaracteristicaSerializer,
    TipoAntiguedadSerializer,
    ImagenesPropiedadSerializer,
    TituloDescripcionPropiedadSerializer,
    UbicacionPropiedadSerializer,
)
from .models import (
    Propiedad,
    TipoPropiedad,
    SubTipoPropiedad,
    TipoAntiguedad,
    Caracteristica,
)
from Avisos.models import Aviso, TipoOperacion
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .Permisions import IsDueño, IsDueñoAviso, maxPropiedades
from rest_framework.generics import ListAPIView, DestroyAPIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser


class TipoPropiedadListView(ListAPIView):
    queryset = TipoPropiedad.objects.all()
    serializer_class = TipoPropiedadSerializer
    permission_classes = [AllowAny]


class SubTipoPropiedadListView(ListAPIView):
    queryset = SubTipoPropiedad.objects.all()
    serializer_class = SubTipoPropiedadSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["tipo_propiedad"]


class TipoOperacionListView(ListAPIView):
    queryset = TipoOperacion.objects.all()
    serializer_class = TipoOperacionSerializer
    permission_classes = [AllowAny]


class PropiedadListView(ListAPIView):
    queryset = Propiedad.objects.all()
    serializer_class = PropiedadListSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination
    filter_backends = [SearchFilter]
    search_fields = [
        "aviso__titulo",
        "aviso__slug",
        "aviso__fecha_creacion",
        "aviso__fecha_actualizacion",
        "aviso__estado__nombre",
        "aviso__tipo_operacion__nombre",
        "tipo_propiedad__nombre",
        "precio_soles",
        "precio_dolares",
    ]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Propiedad.objects.filter(dueño=user)
        return Propiedad.objects.none()


class PropiedadTiposViewSet(viewsets.ModelViewSet):
    queryset = Propiedad.objects.all()
    serializer_class = PropiedadTiposSerializer
    permission_classes = [IsAuthenticated, IsDueño, maxPropiedades]
    http_method_names = [
        "get",
        "post",
        "patch",
    ]


class CaracteristicaListView(ListAPIView):
    queryset = Caracteristica.objects.all()
    serializer_class = CaracteristicaSerializer
    permission_classes = [AllowAny]
    pagination_class = LimitOffsetPagination
    filter_backends = [SearchFilter]
    search_fields = ["nombre"]


class PropiedadDatosViewSet(viewsets.ModelViewSet):
    queryset = Propiedad.objects.all()
    serializer_class = PropiedadDatosSerializer
    permission_classes = [IsAuthenticated, IsDueño]
    http_method_names = [
        "get",
        "patch",
    ]


class EliminarPropiedadView(DestroyAPIView):
    queryset = Propiedad.objects.all()
    serializer_class = PropiedadDatosSerializer
    permission_classes = [IsAuthenticated, IsDueño]
    http_method_names = [
        "delete",
    ]


class TipoAntiguedadListView(ListAPIView):
    queryset = TipoAntiguedad.objects.all()
    serializer_class = TipoAntiguedadSerializer
    permission_classes = [AllowAny]


class ImagenesPropiedadViewSet(viewsets.ModelViewSet):
    queryset = Propiedad.objects.all()
    serializer_class = ImagenesPropiedadSerializer
    permission_classes = [IsAuthenticated, IsDueño]
    # parser_classes = [MultiPartParser, FormParser, JSONParser]
    http_method_names = [
        "get",
        "patch",
    ]


class UbicacionPropiedadViewSet(viewsets.ModelViewSet):
    queryset = Propiedad.objects.all()
    serializer_class = UbicacionPropiedadSerializer
    permission_classes = [IsAuthenticated, IsDueño]
    http_method_names = [
        "get",
        "patch",
    ]


class TituloDescripcionPropiedadViewSet(viewsets.ModelViewSet):
    queryset = Aviso.objects.all()
    serializer_class = TituloDescripcionPropiedadSerializer
    permission_classes = [IsAuthenticated, IsDueñoAviso]
    http_method_names = [
        "get",
        "patch",
    ]
