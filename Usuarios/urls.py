from django.urls import path
from .views import (
    RegistrarUsuarioParticularView,
    RegistrarUsuarioInmobiliariaView,
    VerificarEmail,
    ReenviarEmail,
    IniciarSesion,
    ReestablecerContraseñaPeticion,
    ReestablecerContraseñaConfirmar,
    CambiarContraseña,
    CerrarSesion,
)
from Google.views import GoogleIniciarSesionView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("registrarse-particular/", RegistrarUsuarioParticularView.as_view()),
    path("registrarse-inmobiliaria/", RegistrarUsuarioInmobiliariaView.as_view()),
    path("verificar-email/", VerificarEmail.as_view()),
    path("reenviar-email/", ReenviarEmail.as_view()),
    path("iniciar-sesion/", IniciarSesion.as_view()),
    path("iniciar-sesion/google/", GoogleIniciarSesionView.as_view()),
    path("refrescar-token/", TokenRefreshView.as_view()),
    path("cerrar-sesion/", CerrarSesion.as_view()),
    path(
        "reestablecer-contrasena/",
        ReestablecerContraseñaPeticion.as_view(),
        name="reestablecer-contrasena",
    ),
    path(
        "confirmar-reestablecer-contrasena/<uidb64>/<token>/",
        ReestablecerContraseñaConfirmar.as_view(),
        name="confirmar-reestablecer-contrasena",
    ),
    path("cambiar-contrasena/", CambiarContraseña.as_view()),
]
