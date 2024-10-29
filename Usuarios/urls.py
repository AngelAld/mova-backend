from django.urls import path
from .views import (
    ListaEmpleadosView,
    RegistrarUsuarioEmpleadoView,
    ActualizarEmpleadoView,
    DestroyEmpleadoView,
    RegistrarUsuarioParticularView,
    RegistrarUsuarioInmobiliariaView,
    VerificarEmail,
    ReenviarEmail,
    IniciarSesion,
    ReestablecerContraseñaPeticion,
    ReestablecerContraseñaConfirmar,
    CambiarContraseña,
    CerrarSesion,
    InfoEmpleados,
)
from Google.views import GoogleIniciarSesionView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("registrarse-particular/", RegistrarUsuarioParticularView.as_view()),
    path("registrarse-inmobiliaria/", RegistrarUsuarioInmobiliariaView.as_view()),
    path("empleados/info/", InfoEmpleados.as_view()),
    path("empleados/lista/", ListaEmpleadosView.as_view()),
    path("empleado/nuevo/", RegistrarUsuarioEmpleadoView.as_view()),
    path("empleado/<int:pk>/", ActualizarEmpleadoView.as_view()),
    path("empleado/eliminar/<int:pk>/", DestroyEmpleadoView.as_view()),
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
