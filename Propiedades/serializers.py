from operator import truediv
from os import read
import re
from typing import Required
from Avisos.tasks import CompareAlertaAvisoPropiedad
from Ubicacion.models import Departamento, Provincia
from .models import (
    Caracteristica,
    TipoAntiguedad,
    TipoPropiedad,
    SubTipoPropiedad,
    Propiedad,
    ImagenPropiedad,
    PlanoPropiedad,
    UbicacionPropiedad,
)
from Avisos.models import EstadoAviso, TipoOperacion, Aviso
from rest_framework import serializers
from django.db.transaction import atomic
from drf_extra_fields.fields import Base64ImageField
from django.utils.timezone import now

# Necesitamos registrar la propiedad por partes

# 1. Registrar el tipo de propiedad, el subtipo de propiedad y el tipo de operación
# 2. Registrar datos y caracteristicas de la propiedad
# 3. Registrar ubicación de la propiedad
# 4. Registrar imagenes y planos de la propiedad


# Primero Listamos las propiedades de un usuario


class PropiedadListSerializer(serializers.ModelSerializer):
    cover = serializers.ImageField(source="cover.imagen", read_only=True)
    titulo = serializers.CharField(source="aviso")
    slug = serializers.StringRelatedField(source="aviso.slug")
    fecha_creacion = serializers.DateTimeField(
        source="aviso.fecha_creacion", format="%Y-%m-%d"
    )
    fecha_actualizacion = serializers.DateTimeField(
        source="aviso.fecha_actualizacion", format="%Y-%m-%d"
    )
    estado = serializers.StringRelatedField(source="aviso.estado.nombre")
    favoritos = serializers.IntegerField(source="aviso.getFavoritos")
    tipo_operacion = serializers.StringRelatedField(
        source="aviso.tipo_operacion.nombre"
    )
    tipo_propiedad = serializers.StringRelatedField(source="tipo_propiedad.nombre")

    class Meta:
        model = Propiedad
        fields = [
            "id",
            "titulo",
            "slug",
            "cover",
            "fecha_creacion",
            "fecha_actualizacion",
            "precio_soles",
            "precio_dolares",
            "estado",
            "tipo_operacion",
            "tipo_propiedad",
            "favoritos",
        ]


# para llenar los selects de los formularios de registro de propiedades


class TipoPropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPropiedad
        fields = ["id", "nombre"]
        extra_kwargs = {"nombre": {"read_only": True}, "id": {"read_only": False}}


class SubTipoPropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTipoPropiedad
        fields = ["id", "nombre"]
        extra_kwargs = {"nombre": {"read_only": True}, "id": {"read_only": False}}


class TipoOperacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoOperacion
        fields = ["id", "nombre"]
        extra_kwargs = {"nombre": {"read_only": True}, "id": {"read_only": False}}


# podemos registrar los tipos de la propiedad


class PropiedadTiposSerializer(serializers.ModelSerializer):

    tipo_operacion = serializers.PrimaryKeyRelatedField(
        queryset=TipoOperacion.objects.all(),
        required=True,
        source="aviso.tipo_operacion",
    )

    class Meta:
        model = Propiedad
        fields = [
            "id",
            "tipo_propiedad",
            "subtipo_propiedad",
            "tipo_operacion",
        ]

    @atomic
    def create(self, validated_data):
        tipo_operacion = validated_data.pop("aviso").pop("tipo_operacion")

        dueño = self.context["request"].user
        propiedad = Propiedad.objects.create(
            dueño=dueño,
            **validated_data,
        )
        estado_aviso, _ = EstadoAviso.objects.get_or_create(nombre="En Borrador")
        aviso = Aviso.objects.create(
            propiedad=propiedad,
            tipo_operacion=tipo_operacion,
            estado=estado_aviso,
        )
        # CompareAlertaAvisoPropiedad.delay_on_commit(aviso.pk)
        return propiedad

    @atomic
    def update(self, instance, validated_data):
        tipo_operacion: TipoOperacion = validated_data.pop("aviso").pop(
            "tipo_operacion"
        )
        instance.tipo_propiedad = validated_data.get(
            "tipo_propiedad", instance.tipo_propiedad
        )
        instance.subtipo_propiedad = validated_data.get(
            "subtipo_propiedad", instance.subtipo_propiedad
        )
        instance.save()
        aviso: Aviso = Aviso.objects.get(propiedad=instance)
        aviso.tipo_operacion = tipo_operacion
        aviso.save()
        # CompareAlertaAvisoPropiedad.delay_on_commit(aviso.pk)
        return instance


# tenemos que obtener las caracteristicas de la propiedad primero


class CaracteristicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caracteristica
        fields = ["id", "nombre"]


class PropiedadDatosSerializer(serializers.ModelSerializer):
    caracteristicas = serializers.PrimaryKeyRelatedField(
        queryset=Caracteristica.objects.all(), many=True
    )

    class Meta:
        model = Propiedad
        fields = [
            "id",
            "habitaciones",
            "baños",
            "pisos",
            "ascensores",
            "estacionamientos",
            "area_construida",
            "area_total",
            "precio_soles",
            "precio_dolares",
            "mantenimiento",
            "tipo_antiguedad",
            "años",
            "caracteristicas",
        ]

    @atomic
    def update(self, instance, validated_data):
        caracteristicas = validated_data.pop("caracteristicas")
        instance.habitaciones = validated_data.get(
            "habitaciones", instance.habitaciones
        )
        instance.baños = validated_data.get("baños", instance.baños)
        instance.pisos = validated_data.get("pisos", instance.pisos)
        instance.ascensores = validated_data.get("ascensores", instance.ascensores)
        instance.estacionamientos = validated_data.get(
            "estacionamientos", instance.estacionamientos
        )
        instance.area_construida = validated_data.get(
            "area_construida", instance.area_construida
        )
        instance.area_total = validated_data.get("area_total", instance.area_total)
        instance.precio_soles = validated_data.get(
            "precio_soles", instance.precio_soles
        )
        instance.precio_dolares = validated_data.get(
            "precio_dolares", instance.precio_dolares
        )
        instance.mantenimiento = validated_data.get(
            "mantenimiento", instance.mantenimiento
        )
        instance.tipo_antiguedad = validated_data.get(
            "tipo_antiguedad", instance.tipo_antiguedad
        )
        instance.años = validated_data.get("años", instance.años)

        aviso: Aviso = Aviso.objects.get(propiedad=instance)
        # aviso.fecha_actualizacion = now()
        # aviso.save()

        instance.save()

        instance.caracteristicas.set(caracteristicas)
        # CompareAlertaAvisoPropiedad.delay_on_commit(aviso.pk)
        return instance


class TipoAntiguedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAntiguedad
        fields = ["id", "nombre"]


# Ahora tenemos que subir las imagenes y los planos:


class ImagenPropiedadSerializer(serializers.ModelSerializer):
    is_new = serializers.BooleanField(default=False)
    imagen_url = serializers.CharField(required=False, source="imagen.url")
    imagen = Base64ImageField(required=False, write_only=True)

    class Meta:
        model = ImagenPropiedad
        fields = [
            "id",
            "index",
            "imagen_url",
            "imagen",
            "titulo",
            "cover",
            "is_new",
        ]
        extra_kwargs = {
            "titulo": {"required": False},
            "id": {"read_only": False, "required": False},
        }


class PlanoPropiedadSerializer(serializers.ModelSerializer):
    is_new = serializers.BooleanField(default=False)
    plano_url = serializers.URLField(required=False, source="plano.url", read_only=True)
    plano = Base64ImageField(required=False, write_only=True)

    class Meta:
        model = PlanoPropiedad
        fields = ["id", "plano", "plano_url", "titulo", "is_new"]
        extra_kwargs = {
            "titulo": {"required": False},
            "id": {"read_only": False, "required": False},
        }


class ImagenesPropiedadSerializer(serializers.ModelSerializer):
    imagenes_data = ImagenPropiedadSerializer(many=True, source="imagenes")
    planos_data = PlanoPropiedadSerializer(many=True, source="planos")

    class Meta:
        model = Propiedad
        fields = ["id", "imagenes_data", "planos_data"]

    @atomic
    def update(self, instance, validated_data):
        imagenes = validated_data.pop("imagenes")

        planos = validated_data.pop("planos")

        new_image_ids = [
            img_data.get("id")
            for img_data in imagenes
            if not img_data.get("is_new", False)
        ]

        new_plano_ids = [
            plano_data.get("id")
            for plano_data in planos
            if not plano_data.get("is_new", False)
        ]

        # Delete images that are not included in the request
        ImagenPropiedad.objects.filter(propiedad=instance).exclude(
            id__in=new_image_ids
        ).delete()

        PlanoPropiedad.objects.filter(propiedad=instance).exclude(
            id__in=new_plano_ids
        ).delete()

        for imagen_data in imagenes:
            is_new = imagen_data.pop("is_new", False)
            if is_new:
                imagen_data.pop("id")
                ImagenPropiedad.objects.create(propiedad=instance, **imagen_data)
            else:
                imagen = ImagenPropiedad.objects.get(id=imagen_data["id"])
                imagen.titulo = imagen_data.get("titulo", imagen.titulo)
                imagen.index = imagen_data.get("index", imagen.index)
                imagen.cover = imagen_data.get("cover", imagen.cover)
                imagen.save()

        for plano_data in planos:
            is_new = plano_data.pop("is_new", False)
            if is_new:
                plano_data.pop("id")
                PlanoPropiedad.objects.create(propiedad=instance, **plano_data)
            else:
                plano = PlanoPropiedad.objects.get(id=plano_data["id"])
                plano.titulo = plano_data.get("titulo", plano.titulo)
                plano.save()

        aviso: Aviso = Aviso.objects.get(propiedad=instance)
        # aviso.fecha_actualizacion = now()
        # aviso.save()
        # CompareAlertaAvisoPropiedad.delay_on_commit(aviso.pk)
        return instance


class UbicacionSerializer(serializers.ModelSerializer):
    departamento = serializers.PrimaryKeyRelatedField(
        queryset=Departamento.objects.all(),
        source="distrito.provincia.departamento",
    )
    provincia = serializers.PrimaryKeyRelatedField(
        queryset=Provincia.objects.all(),
        source="distrito.provincia",
    )

    class Meta:
        model = UbicacionPropiedad
        fields = [
            "calle_numero",
            "latitud",
            "longitud",
            "departamento",
            "provincia",
            "distrito",
        ]
        read_only_fields = ["departamento", "provincia"]

    def validate(self, data):
        print(data)
        if data.get("distrito") is None:
            raise serializers.ValidationError("Debe seleccionar un distrito")
        if data.get("calle_numero") is None:
            raise serializers.ValidationError("Debe ingresar una dirección")
        if data.get("latitud") is None:
            raise serializers.ValidationError("Debe ingresar una latitud")
        if data.get("longitud") is None:
            raise serializers.ValidationError("Debe ingresar una longitud")
        return data


class UbicacionPropiedadSerializer(serializers.ModelSerializer):
    ubicacion = UbicacionSerializer()

    class Meta:
        model = Propiedad
        fields = ["id", "ubicacion"]

    @atomic
    def update(self, instance, validated_data):
        ubicacion_data = validated_data.pop("ubicacion")
        UbicacionPropiedad.objects.update_or_create(
            propiedad=instance,
            defaults={
                "distrito": ubicacion_data.get("distrito"),
                "calle_numero": ubicacion_data.get("calle_numero"),
                "latitud": ubicacion_data.get("latitud"),
                "longitud": ubicacion_data.get("longitud"),
            },
        )
        # aviso: Aviso = Aviso.objects.get(propiedad=instance)
        # aviso.fecha_actualizacion = now()
        # aviso.save()
        # CompareAlertaAvisoPropiedad.delay_on_commit(aviso.pk)
        return instance
