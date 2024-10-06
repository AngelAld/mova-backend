from django.db import models
from Ubicacion.models import Distrito
from Usuarios.models import User


class Caracteristica(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class TipoAntiguedad(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class TipoPropiedad(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class SubTipoPropiedad(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)
    tipo_propiedad = models.ForeignKey(TipoPropiedad, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre


# All fields are null to allow for partial updates
class Propiedad(models.Model):
    dueño = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="propiedades"
    )
    habitaciones = models.PositiveIntegerField(blank=True, null=True, default=0)
    baños = models.PositiveIntegerField(blank=True, null=True, default=0)
    pisos = models.PositiveIntegerField(blank=True, null=True, default=1)
    ascensores = models.PositiveIntegerField(blank=True, null=True, default=0)
    estacionamientos = models.PositiveIntegerField(blank=True, null=True, default=0)
    area_construida = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, default=0
    )
    area_total = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, default=0
    )
    precio_soles = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, default=0
    )
    precio_dolares = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, default=0
    )
    mantenimiento = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, default=0
    )
    tipo_antiguedad = models.ForeignKey(
        TipoAntiguedad, on_delete=models.PROTECT, blank=True, null=True
    )
    años = models.PositiveIntegerField(blank=True, null=True, default=0)
    tipo_propiedad = models.ForeignKey(
        TipoPropiedad,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    subtipo_propiedad = models.ForeignKey(
        SubTipoPropiedad, on_delete=models.PROTECT, blank=True, null=True
    )
    caracteristicas = models.ManyToManyField(Caracteristica, blank=True)

    @property
    def cover(self):
        return ImagenPropiedad.objects.filter(propiedad=self, cover=True).first()

    def __str__(self):
        return f"{self.dueño} - {self.id}"


class ImagenPropiedad(models.Model):
    index = models.PositiveIntegerField(default=0)
    propiedad = models.ForeignKey(
        Propiedad, on_delete=models.CASCADE, related_name="imagenes"
    )
    imagen = models.ImageField(upload_to="propiedades/")
    titulo = models.CharField(max_length=100, blank=True)
    cover = models.BooleanField(default=False)

    def __str__(self):
        return self.imagen.url


class PlanoPropiedad(models.Model):
    propiedad = models.ForeignKey(
        Propiedad, on_delete=models.CASCADE, related_name="planos"
    )
    plano = models.ImageField(upload_to="planos/")
    titulo = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.plano.url


class UbicacionPropiedad(models.Model):
    propiedad = models.OneToOneField(
        Propiedad, on_delete=models.CASCADE, related_name="ubicacion"
    )
    distrito = models.ForeignKey(Distrito, on_delete=models.PROTECT)
    calle_numero = models.CharField(max_length=100)
    latitud = models.FloatField()
    longitud = models.FloatField()

    @property
    def direccion(self):
        return f"{self.distrito.provincia.nombre}, {self.distrito.nombre}"

    def __str__(self):
        return f"{self.distrito}, {self.calle_numero}"
