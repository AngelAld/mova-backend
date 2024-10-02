from datetime import date
import datetime
from django.db import models
from Propiedades.models import Propiedad
from Usuarios.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.timezone import now
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
        if not self.slug:
            slug = slugify(self.titulo or "propiedad")
            original_slug = slug
            counter = 1
            while Aviso.objects.filter(slug=slug).exists():
                slug = f"{original_slug}-{counter}"
                counter += 1
            self.slug = slug

        super(Aviso, self).save(**kwargs)

    def update(self, **kwargs):
        previous_slug = self.slug
        slug = slugify(self.titulo or "propiedad")

        if previous_slug != slug:
            original_slug = slug
            counter = 1
            while Aviso.objects.filter(slug=slug).exists():
                slug = f"{original_slug}-{counter}"
                counter += 1
            self.slug = slug

        super(Aviso, self).update(**kwargs)

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
