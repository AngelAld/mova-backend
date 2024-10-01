from pyexpat import model

from attrs import field
from Propiedades.models import UbicacionPropiedad
from Usuarios.models import User
from .models import Aviso, EstadoAviso, TipoOperacion, Favorito
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
