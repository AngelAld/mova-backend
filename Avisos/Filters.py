from django_filters import FilterSet, RangeFilter, DateFromToRangeFilter
from .models import Aviso
from Propiedades.models import Propiedad
from django_filters.rest_framework import CharFilter
from django.db.models import Count, Q


class AvisoFilter(FilterSet):
    propiedad__precio_soles = RangeFilter()
    propiedad__precio_dolares = RangeFilter()
    propiedad__habitaciones = RangeFilter()
    propiedad__baños = RangeFilter()
    propiedad__pisos = RangeFilter()
    propiedad__ascensores = RangeFilter()
    propiedad__estacionamientos = RangeFilter()
    propiedad__area_total = RangeFilter()
    propiedad__area_construida = RangeFilter()
    propiedad__mantenimiento = RangeFilter()
    # fecha_actualizacion = DateFromToRangeFilter()
    propiedad__caracteristicas = CharFilter(method="filter_caracteristicas")
    propiedad__ubicacion__distrito = CharFilter(method="filter_distrito")
    propiedad__ubicacion__distrito__provincia = CharFilter(method="filter_provincia")
    propiedad__ubicacion__distrito__provincia__departamento = CharFilter(
        method="filter_departamento"
    )

    class Meta:
        model = Aviso
        fields = [
            "propiedad__precio_soles",
            "propiedad__precio_dolares",
            "propiedad__habitaciones",
            "propiedad__baños",
            "propiedad__ascensores",
            "propiedad__pisos",
            "propiedad__estacionamientos",
            "propiedad__area_total",
            "propiedad__area_construida",
            "propiedad__mantenimiento",
            "tipo_operacion",
            "propiedad__tipo_antiguedad",
            "propiedad__subtipo_propiedad",
            "propiedad__tipo_propiedad",
            "propiedad__caracteristicas",
            "propiedad__ubicacion__distrito",
            "propiedad__ubicacion__distrito__provincia",
            "propiedad__ubicacion__distrito__provincia__departamento",
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

    def filter_distrito(self, queryset, name, value):
        pks = value.split(",")
        queryset = queryset.filter(propiedad__ubicacion__distrito__pk__in=pks)
        return queryset

    def filter_provincia(self, queryset, name, value):
        pks = value.split(",")
        queryset = queryset.filter(
            propiedad__ubicacion__distrito__provincia__pk__in=pks
        )
        return queryset

    def filter_departamento(self, queryset, name, value):
        pks = value.split(",")
        queryset = queryset.filter(
            propiedad__ubicacion__distrito__provincia__departamento__pk__in=pks
        )
        return queryset
