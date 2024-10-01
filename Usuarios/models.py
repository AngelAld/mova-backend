from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .manager import UserManager
from rest_framework_simplejwt.tokens import RefreshToken
from Planes.models import Plan


AUTH_PROVIDERS = {
    "email": "email",
    "google": "google",
}


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        max_length=255, unique=True, verbose_name=_("Correo electrónico")
    )
    nombres = models.CharField(max_length=255, verbose_name=_("Nombres"))
    apellidos = models.CharField(max_length=255, verbose_name=_("Apellidos"))
    is_inmobiliaria = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    provider = models.CharField(max_length=255, default=AUTH_PROVIDERS.get("email"))

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nombres", "apellidos"]

    objects = UserManager()

    class Meta:
        verbose_name = _("Usuario")
        verbose_name_plural = _("Usuarios")

    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        return f"{self.nombres} {self.apellidos}"

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {"refresh": str(refresh), "access": str(refresh.access_token)}


class OneTimePassword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)


class PerfilParticular(models.Model):
    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="perfil_particular"
    )
    dni = models.CharField(max_length=8, unique=True)
    telefono = models.CharField(max_length=9)
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT)

    def __str__(self):
        return self.usuario.get_full_name


class PerfilInmobiliaria(models.Model):
    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="perfil_inmobiliaria"
    )
    razon_social = models.CharField(max_length=255)
    ruc = models.CharField(max_length=11, unique=True)
    telefono = models.CharField(max_length=9)
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT)
    aprobada = models.BooleanField(default=False)

    def __str__(self):
        return self.razon_social


class PerfilEmpleado(models.Model):
    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="perfil_empleado"
    )
    dni = models.CharField(max_length=8, unique=True)
    telefono = models.CharField(max_length=9)
    inmobiliaria = models.ForeignKey(
        PerfilInmobiliaria, on_delete=models.CASCADE, related_name="empleados"
    )

    def __str__(self):
        return self.usuario.get_full_name
