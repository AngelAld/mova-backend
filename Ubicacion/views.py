from .models import Departamento, Provincia, Distrito
from .serializers import DepartamentoSerializer, ProvinciaSerializer, DistritoSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination


class DepartamentoListView(ListAPIView):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    filter_backends = [SearchFilter]
    pagination_class = LimitOffsetPagination
    search_fields = ["nombre"]


class ProvinciaListView(ListAPIView):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    pagination_class = LimitOffsetPagination
    filterset_fields = ["departamento"]
    search_fields = ["nombre"]


class DistritoListView(ListAPIView):
    queryset = Distrito.objects.all()
    serializer_class = DistritoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    pagination_class = LimitOffsetPagination
    filterset_fields = ["provincia"]
    search_fields = ["nombre"]
