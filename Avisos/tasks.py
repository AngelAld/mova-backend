from django.db.models import Q
from Avisos.models import Alerta, Aviso, AvisoAlerta
from celery import shared_task
from typing import List
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task
def CompareAlertaAvisoPropiedad(pk: int):
    aviso = Aviso.objects.get(pk=pk)
    alertas = filter_alertas(aviso)
    process_alertas(alertas, aviso)


def filter_alertas(aviso: Aviso) -> List[Alerta]:
    propiedad = aviso.propiedad

    # Start with all alerts
    alertas = Alerta.objects.all()

    # Filter by tipo_operacion
    if aviso.tipo_operacion:
        alertas = alertas.filter(
            Q(tipo_operacion=aviso.tipo_operacion) | Q(tipo_operacion__isnull=True)
        )

    # Filter by precio_soles
    if propiedad.precio_soles:
        alertas = alertas.filter(
            Q(propiedad_precio_soles_min__lte=propiedad.precio_soles)
            & Q(propiedad_precio_soles_max__gte=propiedad.precio_soles)
            | Q(propiedad_precio_soles_min__isnull=True)
            & Q(propiedad_precio_soles_max__isnull=True)
        )

    # Filter by precio_dolares
    if propiedad.precio_dolares:
        alertas = alertas.filter(
            Q(propiedad_precio_dolares_min__lte=propiedad.precio_dolares)
            & Q(propiedad_precio_dolares_max__gte=propiedad.precio_dolares)
            | Q(propiedad_precio_dolares_min__isnull=True)
            & Q(propiedad_precio_dolares_max__isnull=True)
        )

    # Filter by habitaciones
    if propiedad.habitaciones:
        alertas = alertas.filter(
            Q(propiedad_habitaciones_min__lte=propiedad.habitaciones)
            & Q(propiedad_habitaciones_max__gte=propiedad.habitaciones)
            | Q(propiedad_habitaciones_min__isnull=True)
            & Q(propiedad_habitaciones_max__isnull=True)
        )

    # Filter by baños
    if propiedad.baños:
        alertas = alertas.filter(
            Q(propiedad_baños_min__lte=propiedad.baños)
            & Q(propiedad_baños_max__gte=propiedad.baños)
            | Q(propiedad_baños_min__isnull=True) & Q(propiedad_baños_max__isnull=True)
        )

    # Filter by ascensores
    if propiedad.ascensores:
        alertas = alertas.filter(
            Q(propiedad_ascensores_min__lte=propiedad.ascensores)
            & Q(propiedad_ascensores_max__gte=propiedad.ascensores)
            | Q(propiedad_ascensores_min__isnull=True)
            & Q(propiedad_ascensores_max__isnull=True)
        )

    # Filter by pisos
    if propiedad.pisos:
        alertas = alertas.filter(
            Q(propiedad_pisos_min__lte=propiedad.pisos)
            & Q(propiedad_pisos_max__gte=propiedad.pisos)
            | Q(propiedad_pisos_min__isnull=True) & Q(propiedad_pisos_max__isnull=True)
        )

    # Filter by estacionamientos
    if propiedad.estacionamientos:
        alertas = alertas.filter(
            Q(propiedad_estacionamientos_min__lte=propiedad.estacionamientos)
            & Q(propiedad_estacionamientos_max__gte=propiedad.estacionamientos)
            | Q(propiedad_estacionamientos_min__isnull=True)
            & Q(propiedad_estacionamientos_max__isnull=True)
        )

    # Filter by area_total
    if propiedad.area_total:
        alertas = alertas.filter(
            Q(propiedad_area_total_min__lte=propiedad.area_total)
            & Q(propiedad_area_total_max__gte=propiedad.area_total)
            | Q(propiedad_area_total_min__isnull=True)
            & Q(propiedad_area_total_max__isnull=True)
        )

    # Filter by area_construida
    if propiedad.area_construida:
        alertas = alertas.filter(
            Q(propiedad_area_construida_min__lte=propiedad.area_construida)
            & Q(propiedad_area_construida_max__gte=propiedad.area_construida)
            | Q(propiedad_area_construida_min__isnull=True)
            & Q(propiedad_area_construida_max__isnull=True)
        )

    # Filter by mantenimiento
    if propiedad.mantenimiento:
        alertas = alertas.filter(
            Q(propiedad_mantenimiento_min__lte=propiedad.mantenimiento)
            & Q(propiedad_mantenimiento_max__gte=propiedad.mantenimiento)
            | Q(propiedad_mantenimiento_min__isnull=True)
            & Q(propiedad_mantenimiento_max__isnull=True)
        )

    # Filter by tipo_antiguedad
    if propiedad.tipo_antiguedad:
        alertas = alertas.filter(
            Q(propiedad_tipo_antiguedad=propiedad.tipo_antiguedad)
            | Q(propiedad_tipo_antiguedad__isnull=True)
        )

    # Filter by subtipo_propiedad
    if propiedad.subtipo_propiedad:
        alertas = alertas.filter(
            Q(propiedad_subtipo_propiedad=propiedad.subtipo_propiedad)
            | Q(propiedad_subtipo_propiedad__isnull=True)
        )

    # Filter by tipo_propiedad
    if propiedad.tipo_propiedad:
        alertas = alertas.filter(
            Q(propiedad_tipo_propiedad=propiedad.tipo_propiedad)
            | Q(propiedad_tipo_propiedad__isnull=True)
        )

    # Filter by caracteristicas
    if propiedad.caracteristicas.exists():
        propiedad_caracteristicas = set(
            propiedad.caracteristicas.values_list("nombre", flat=True)
        )
        alertas = alertas.filter(
            Q(propiedad_caracteristicas__contains=list(propiedad_caracteristicas))
            | Q(propiedad_caracteristicas=[])
        )

    return list(alertas)


def get_value(value, default):
    return value if value is not None else default


def process_alertas(alertas: List[Alerta], aviso: Aviso):
    for alerta in alertas:
        _, _ = AvisoAlerta.objects.get_or_create(alerta=alerta, aviso=aviso)
