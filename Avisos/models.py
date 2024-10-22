from django.db import models
from Propiedades.models import (
    Propiedad,
    SubTipoPropiedad,
    TipoAntiguedad,
    TipoPropiedad,
)
from Ubicacion.models import Departamento, Distrito, Provincia
from Usuarios.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.text import slugify


class TipoOperacion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class EstadoAviso(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class Aviso(models.Model):
    propiedad = models.OneToOneField(
        Propiedad, on_delete=models.CASCADE, related_name="aviso"
    )
    titulo = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(10), MaxLengthValidator(100)],
        blank=True,
        null=True,
    )
    slug = models.SlugField(max_length=100, unique=True, editable=False)
    descripcion = models.TextField(blank=True, null=True)
    tipo_operacion = models.ForeignKey(TipoOperacion, on_delete=models.PROTECT)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.ForeignKey(EstadoAviso, on_delete=models.PROTECT)

    @property
    def getFavoritos(self):
        return self.favoritos.count()

    def save(self, **kwargs):
        slug_base = slugify(self.titulo or "propiedad")
        if not self.slug or self.slug != slug_base:
            slug = slug_base
            original_slug = slug
            counter = 1
            while Aviso.objects.filter(slug=slug).exists():
                slug = f"{original_slug}-{counter}"
                counter += 1
            self.slug = slug

        super(Aviso, self).save(**kwargs)

    # def update(self, **kwargs):
    #     previous_slug = self.slug
    #     slug = slugify(self.titulo or "propiedad")

    #     if previous_slug != slug:
    #         original_slug = slug
    #         counter = 1
    #         while Aviso.objects.filter(slug=slug).exists():
    #             slug = f"{original_slug}-{counter}"
    #             counter += 1
    #         self.slug = slug

    #     super(Aviso, self).update(**kwargs)

    def __str__(self):
        if self.titulo:
            return self.titulo
        return "Propiedad sin titulo"


class Favorito(models.Model):
    aviso = models.ForeignKey(Aviso, on_delete=models.CASCADE, related_name="favoritos")
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="favoritos"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)


class Alerta(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="alertas")
    propiedad_precio_soles_min = models.DecimalField(
        max_digits=12, decimal_places=2, default=0
    )
    propiedad_precio_soles_max = models.DecimalField(
        max_digits=12, decimal_places=2, default=1000000
    )
    propiedad_precio_dolares_min = models.DecimalField(
        max_digits=12, decimal_places=2, default=0
    )
    propiedad_precio_dolares_max = models.DecimalField(
        max_digits=12, decimal_places=2, default=1000000
    )
    propiedad_habitaciones_min = models.IntegerField(default=0)
    propiedad_habitaciones_max = models.IntegerField(default=30)
    propiedad_baños_min = models.IntegerField(default=0)
    propiedad_baños_max = models.IntegerField(default=30)
    propiedad_ascensores_min = models.IntegerField(default=0)
    propiedad_ascensores_max = models.IntegerField(default=10)
    propiedad_pisos_min = models.IntegerField(default=0)
    propiedad_pisos_max = models.IntegerField(default=100)
    propiedad_estacionamientos_min = models.IntegerField(default=0)
    propiedad_estacionamientos_max = models.IntegerField(default=30)
    propiedad_area_total_min = models.DecimalField(
        max_digits=12, decimal_places=2, default=0
    )
    propiedad_area_total_max = models.DecimalField(
        max_digits=12, decimal_places=2, default=2000
    )
    propiedad_area_construida_min = models.DecimalField(
        max_digits=12, decimal_places=2, default=0
    )
    propiedad_area_construida_max = models.DecimalField(
        max_digits=12, decimal_places=2, default=2000
    )
    propiedad_mantenimiento_min = models.DecimalField(
        max_digits=12, decimal_places=2, default=0
    )
    propiedad_mantenimiento_max = models.DecimalField(
        max_digits=12, decimal_places=2, default=10000
    )
    tipo_operacion = models.ForeignKey(
        TipoOperacion, on_delete=models.CASCADE, blank=True, null=True
    )
    propiedad_tipo_antiguedad = models.ForeignKey(
        TipoAntiguedad, on_delete=models.CASCADE, blank=True, null=True
    )
    propiedad_subtipo_propiedad = models.ForeignKey(
        SubTipoPropiedad, on_delete=models.CASCADE, null=True, blank=True
    )
    propiedad_tipo_propiedad = models.ForeignKey(
        TipoPropiedad, null=True, blank=True, on_delete=models.CASCADE
    )
    propiedad_ubicacion_distrito = models.ForeignKey(
        Distrito, null=True, blank=True, on_delete=models.CASCADE
    )
    propiedad_ubicacion_distrito_provincia = models.ForeignKey(
        Provincia, null=True, blank=True, on_delete=models.CASCADE
    )
    propiedad_ubicacion_distrito_provincia_departamento = models.ForeignKey(
        Departamento, null=True, blank=True, on_delete=models.CASCADE
    )
    propiedad_caracteristicas = models.JSONField(default=list, blank=True)


class AvisoAlerta(models.Model):
    alerta = models.ForeignKey(Alerta, on_delete=models.CASCADE, related_name="avisos")
    aviso = models.ForeignKey(Aviso, on_delete=models.CASCADE, related_name="alertas")
