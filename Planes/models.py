from tabnanny import verbose
from django.db import models


# Create your models here.
class Plan(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Nombre")
    descripcion = models.TextField(verbose_name="Descripción", blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    num_propiedades = models.IntegerField(verbose_name="Número de propiedades")
    num_empleados = models.IntegerField(verbose_name="Número de empleados")
    compartir_comision = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Plan"
        verbose_name_plural = "Planes"

    def __str__(self):
        return f"{self.nombre} - S./{self.precio}"
