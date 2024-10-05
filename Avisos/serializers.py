from os import read
from pyexpat import model
from django.db.transaction import atomic
from attrs import field
from Propiedades.models import UbicacionPropiedad
from Usuarios.models import User
from .models import Aviso, EstadoAviso, TipoOperacion, Favorito, Alerta, AvisoAlerta
from Propiedades.models import ImagenPropiedad, PlanoPropiedad, Propiedad
from rest_framework import serializers


class AvisoListaSerializer(serializers.ModelSerializer):

    direccion = serializers.CharField(source="propiedad.ubicacion.calle_numero")

    distrito = serializers.CharField(source="propiedad.ubicacion.distrito.nombre")

    estado = serializers.CharField(source="estado.nombre")
    tipo_operacion = serializers.CharField(
        source="tipo_operacion.nombre", allow_null=True
    )

    habitaciones = serializers.IntegerField(
        source="propiedad.habitaciones", allow_null=True
    )

    area_total = serializers.DecimalField(
        source="propiedad.area_total", max_digits=10, decimal_places=2, allow_null=True
    )
    precio_soles = serializers.DecimalField(
        source="propiedad.precio_soles",
        max_digits=10,
        decimal_places=2,
        allow_null=True,
    )
    precio_dolares = serializers.DecimalField(
        source="propiedad.precio_dolares",
        max_digits=10,
        decimal_places=2,
        allow_null=True,
    )
    tipo_antiguedad = serializers.CharField(
        source="propiedad.tipo_antiguedad.nombre", allow_null=True
    )
    años = serializers.IntegerField(source="propiedad.años", allow_null=True)

    subtipo_propiedad = serializers.CharField(
        source="propiedad.subtipo_propiedad.nombre", allow_null=True
    )
    caracteristicas = serializers.StringRelatedField(
        many=True, source="propiedad.caracteristicas"
    )
    cover = serializers.StringRelatedField(source="propiedad.cover")

    fecha_actualizacion = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = Aviso
        fields = [
            "slug",
            "titulo",
            "cover",
            "estado",
            "direccion",
            "distrito",
            "descripcion",
            "tipo_operacion",
            "fecha_actualizacion",
            "habitaciones",
            "area_total",
            "precio_soles",
            "precio_dolares",
            "tipo_antiguedad",
            "años",
            "subtipo_propiedad",
            "caracteristicas",
        ]


class DueñoSerializer(serializers.ModelSerializer):

    nombre = serializers.SerializerMethodField()
    telefono = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["nombre", "email", "telefono"]

    def get_nombre(self, obj):
        if hasattr(obj, "perfil_particular"):
            return obj.perfil_particular.usuario.get_full_name
        elif hasattr(obj, "perfil_empleado"):
            return obj.perfil_empleado.inmobiliaria.razon_social
        elif hasattr(obj, "perfil_inmobiliaria"):
            return obj.perfil_inmobiliaria.razon_social
        else:
            return None

    def get_telefono(self, obj):
        if hasattr(obj, "perfil_particular"):
            return obj.perfil_particular.telefono
        elif hasattr(obj, "perfil_empleado"):
            return obj.perfil_empleado.inmobiliaria.telefono
        elif hasattr(obj, "perfil_inmobiliaria"):
            return obj.perfil_inmobiliaria.telefono
        else:
            return None


class ImagenesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImagenPropiedad
        fields = ["index", "imagen", "titulo"]


class PlanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanoPropiedad
        fields = ["plano", "titulo"]


class UbicacionSerializer(serializers.ModelSerializer):
    distrito = serializers.CharField(source="distrito.nombre")
    provincia = serializers.CharField(source="distrito.provincia.nombre")

    class Meta:
        model = UbicacionPropiedad
        fields = ["provincia", "distrito", "calle_numero", "latitud", "longitud"]


class AvisoDetalleSerializer(serializers.ModelSerializer):

    ubicacion = UbicacionSerializer(source="propiedad.ubicacion", read_only=True)

    imagenes = ImagenesSerializer(
        source="propiedad.imagenes", read_only=True, many=True
    )

    planos = PlanoSerializer(source="propiedad.planos", read_only=True, many=True)

    dueño = DueñoSerializer(source="propiedad.dueño", read_only=True, many=False)

    tipo_operacion = serializers.CharField(
        source="tipo_operacion.nombre", allow_null=True
    )

    habitaciones = serializers.IntegerField(
        source="propiedad.habitaciones", allow_null=True
    )

    area_total = serializers.DecimalField(
        source="propiedad.area_total", max_digits=10, decimal_places=2, allow_null=True
    )

    area_construida = serializers.DecimalField(
        source="propiedad.area_construida",
        max_digits=10,
        decimal_places=2,
        allow_null=True,
    )
    precio_soles = serializers.DecimalField(
        source="propiedad.precio_soles",
        max_digits=10,
        decimal_places=2,
        allow_null=True,
    )
    precio_dolares = serializers.DecimalField(
        source="propiedad.precio_dolares",
        max_digits=10,
        decimal_places=2,
        allow_null=True,
    )
    tipo_antiguedad = serializers.CharField(
        source="propiedad.tipo_antiguedad.nombre", allow_null=True
    )
    años = serializers.IntegerField(source="propiedad.años", allow_null=True)

    subtipo_propiedad = serializers.CharField(
        source="propiedad.subtipo_propiedad.nombre", allow_null=True
    )
    caracteristicas = serializers.StringRelatedField(
        many=True, source="propiedad.caracteristicas"
    )

    fecha_actualizacion = serializers.DateTimeField(format="%Y-%m-%d")

    baños = serializers.IntegerField(source="propiedad.baños", allow_null=True)

    pisos = serializers.IntegerField(source="propiedad.pisos", allow_null=True)

    ascensores = serializers.IntegerField(
        source="propiedad.ascensores", allow_null=True
    )

    estacionamientos = serializers.IntegerField(
        source="propiedad.estacionamientos", allow_null=True
    )

    mantenimiento = serializers.DecimalField(
        source="propiedad.mantenimiento",
        max_digits=10,
        decimal_places=2,
        allow_null=True,
    )

    class Meta:
        model = Aviso
        fields = [
            "slug",
            "titulo",
            "dueño",
            "descripcion",
            "tipo_operacion",
            "fecha_actualizacion",
            "habitaciones",
            "baños",
            "pisos",
            "ascensores",
            "estacionamientos",
            "area_total",
            "area_construida",
            "precio_soles",
            "precio_dolares",
            "mantenimiento",
            "tipo_antiguedad",
            "años",
            "subtipo_propiedad",
            "caracteristicas",
            "imagenes",
            "planos",
            "ubicacion",
        ]


class AlertaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alerta
        fields = "__all__"
        read_only_fields = ["user"]

    def validate(self, attrs):
        if attrs["propiedad_precio_soles_min"] > attrs["propiedad_precio_soles_max"]:
            raise serializers.ValidationError(
                "El precio mínimo no puede ser mayor al precio máximo"
            )
        if (
            attrs["propiedad_precio_dolares_min"]
            > attrs["propiedad_precio_dolares_max"]
        ):
            raise serializers.ValidationError(
                "El precio mínimo no puede ser mayor al precio máximo"
            )
        if attrs["propiedad_habitaciones_min"] > attrs["propiedad_habitaciones_max"]:
            raise serializers.ValidationError(
                "El número mínimo de habitaciones no puede ser mayor al número máximo de habitaciones"
            )
        if attrs["propiedad_banos_min"] > attrs["propiedad_banos_max"]:
            raise serializers.ValidationError(
                "El número mínimo de baños no puede ser mayor al número máximo de baños"
            )
        if attrs["propiedad_ascensores_min"] > attrs["propiedad_ascensores_max"]:
            raise serializers.ValidationError(
                "El número mínimo de ascensores no puede ser mayor al número máximo de ascensores"
            )
        if attrs["propiedad_pisos_min"] > attrs["propiedad_pisos_max"]:
            raise serializers.ValidationError(
                "El número mínimo de pisos no puede ser mayor al número máximo de pisos"
            )
        if (
            attrs["propiedad_estacionamientos_min"]
            > attrs["propiedad_estacionamientos_max"]
        ):
            raise serializers.ValidationError(
                "El número mínimo de estacionamientos no puede ser mayor al número máximo de estacionamientos"
            )
        if attrs["propiedad_area_total_min"] > attrs["propiedad_area_total_max"]:
            raise serializers.ValidationError(
                "El área total mínima no puede ser mayor al área total máxima"
            )
        if (
            attrs["propiedad_area_construida_min"]
            > attrs["propiedad_area_construida_max"]
        ):
            raise serializers.ValidationError(
                "El área construida mínima no puede ser mayor al área construida máxima"
            )
        if attrs["propiedad_mantenimiento_min"] > attrs["propiedad_mantenimiento_max"]:
            raise serializers.ValidationError(
                "El mantenimiento mínimo no puede ser mayor al mantenimiento máximo"
            )
        return super().validate(attrs)


class AlertaAvisoListSerializer(serializers.ModelSerializer):
    avisos = AvisoListaSerializer(many=True, source="avisos")

    class Meta:
        model = Alerta
        fields = ["id", "avisos"]
