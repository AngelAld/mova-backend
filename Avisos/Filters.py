from django_filters import FilterSet, RangeFilter, DateFromToRangeFilter
from .models import Aviso
from Propiedades.models import Propiedad
from django_filters.rest_framework import CharFilter
from django.db.models import Count, Q


class AvisoFilter(FilterSet):
    propiedad__precio_soles = RangeFilter()
    propiedad__precio_dolares = RangeFilter()
    # fecha_actualizacion = DateFromToRangeFilter()
    propiedad__caracteristicas = CharFilter(method="filter_caracteristicas")

    class Meta:
        model = Aviso
        fields = [
            "propiedad__precio_soles",
            "propiedad__precio_dolares",
            "estado",
            "tipo_operacion",
            "propiedad__tipo_antiguedad",
            "propiedad__subtipo_propiedad",
            "propiedad__caracteristicas",
            # "fecha_actualizacion",
        ]

    def filter_caracteristicas(self, queryset, name, value):
        pks = value.split(",")
        queryset = queryset.annotate(
            num_caracteristicas=Count(
                "propiedad__caracteristicas",
                filter=Q(propiedad__caracteristicas__pk__in=pks),
            )
        )
        filtered_queryset = queryset.filter(num_caracteristicas=len(pks)).distinct()
        return filtered_queryset
