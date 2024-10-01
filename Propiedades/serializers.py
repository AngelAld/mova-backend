from email.mime import image
from operator import is_
from os import read, write
from re import A
from tkinter import Image

from django.forms import IntegerField

import Avisos
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
        Aviso.objects.create(
            propiedad=propiedad,
            tipo_operacion=tipo_operacion,
            estado=estado_aviso,
        )
        return propiedad

    @atomic
    def update(self, instance, validated_data):

        tipo_operacion: TipoOperacion = validated_data.pop("aviso").pop(
            "tipo_operacion"
        )
        print("paso 1")
        instance.tipo_propiedad = validated_data.get(
            "tipo_propiedad", instance.tipo_propiedad
        )
        print("paso 2")
        instance.subtipo_propiedad = validated_data.get(
            "subtipo_propiedad", instance.subtipo_propiedad
        )
        print("paso 3")

        instance.save()
        print("paso 4")
        aviso: Aviso = Aviso.objects.get(propiedad=instance)
        print("paso 5")
        aviso.tipo_operacion = tipo_operacion
        print("paso 6")
        aviso.save()
        print("paso 7")
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
        instance.save()

        instance.caracteristicas.set(caracteristicas)
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


# class PlanoPropiedadSerializer(serializers.ModelSerializer):
#     is_new = serializers.BooleanField(default=False)
#     plano_url = serializers.URLField(required=False, source="plano.url", read_only=True)
#     imagen = serializers.bas

#     class Meta:
#         model = PlanoPropiedad
#         fields = ["id", "plano", "plano_url", "titulo", "is_new"]
#         extra_kwargs = {
#             "plano": {"required": False, "write_only": True},
#             "titulo": {"required": False},
#             "id": {"read_only": False, "required": False},
#         }

#         def validate(self, attrs):
#             if not attrs.get("plano") and not attrs.get("is_new"):
#                 raise serializers.ValidationError("Plano no puede ser vacío")
#             return attrs


class ImagenesPropiedadSerializer(serializers.ModelSerializer):
    imagenes_data = ImagenPropiedadSerializer(many=True, source="imagenes")
    # planos_data = PlanoPropiedadSerializer(many=True, source="planos")

    class Meta:
        model = Propiedad
        fields = ["id", "imagenes_data"]

    def validate(self, attrs):
        print("####################")
        print(attrs)
        print("####################")
        return super().validate(attrs)

    @atomic
    def update(self, instance, validated_data):
        imagenes = validated_data.pop("imagenes")

        # planos = validated_data.pop("planos")

        # Get the IDs of the images included in the request
        new_image_ids = [
            img_data.get("id")
            for img_data in imagenes
            if not img_data.get("is_new", False)
        ]

        # Delete images that are not included in the request
        ImagenPropiedad.objects.filter(propiedad=instance).exclude(
            id__in=new_image_ids
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

        return instance

        # for plano_data in planos:
        #     is_new = plano_data.pop("is_new")
        #     if is_new:
        #         PlanoPropiedad.objects.create(propiedad=instance, **plano_data)
        #     else:
        #         plano = PlanoPropiedad.objects.get(id=plano_data["id"])
        #         plano.titulo = plano_data.get("titulo", plano.titulo)
        #         plano.save()
        # return instance
