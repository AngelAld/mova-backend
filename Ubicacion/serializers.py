from attr import fields
from rest_framework import serializers
from .models import Departamento, Provincia, Distrito


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ["id", "nombre"]


class ProvinciaSerializer(serializers.ModelSerializer):
    nombre_completo = serializers.SerializerMethodField()

    class Meta:
        model = Provincia
        fields = ["id", "nombre", "nombre_completo"]

    def get_nombre_completo(self, obj):
        return f"{obj.nombre}, {obj.departamento.nombre}"


class DistritoSerializer(serializers.ModelSerializer):
    nombre_completo = serializers.SerializerMethodField()

    class Meta:
        model = Distrito
        fields = ["id", "nombre", "nombre_completo"]

    def get_nombre_completo(self, obj):
        return (
            f"{obj.nombre}, {obj.provincia.nombre}, {obj.provincia.departamento.nombre}"
        )
