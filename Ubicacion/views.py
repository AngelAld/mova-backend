from .models import Departamento, Provincia, Distrito
from .serializers import DepartamentoSerializer, ProvinciaSerializer, DistritoSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend


class DepartamentoListView(ListAPIView):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer


class ProvinciaListView(ListAPIView):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["departamento"]


class DistritoListView(ListAPIView):
    queryset = Distrito.objects.all()
    serializer_class = DistritoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["provincia"]
