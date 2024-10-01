from google.auth.transport import requests
from google.oauth2 import id_token
from Usuarios.models import User
from django.contrib.auth import authenticate
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed


class Google:
    @staticmethod
    def validar(access):
        try:
            id_info = id_token.verify_oauth2_token(access, requests.Request())
            if "accounts.google.com" in id_info["iss"]:
                return id_info
        except Exception as e:
            return "Error al validar el token de Google"


def iniciarSesion(email, password):
    user = authenticate(email=email, password=password)
    if not user:
        raise AuthenticationFailed("Credenciales incorrectas, intente de nuevo")
    token = user.tokens()

    return {
        "email": user.email,
        "nombres": user.nombres,
        "apellidos": user.apellidos,
        "access": str(token["access"]),
        "refresh": str(token["refresh"]),
    }


def registrarUsuarioGoogle(provider, email, nombres, apellidos):
    user = User.objects.filter(email=email)
    if user.exists():
        user = user.first()
        if user.provider != provider:
            raise AuthenticationFailed(f"Por favor, inicie sesión con {user.provider}")
        user = iniciarSesion(email=email, password=settings.SOCIAL_AUTH_PASSWORD)
        return user
    else:
        user = User.objects.create_user(
            email=email,
            nombres=nombres,
            apellidos=apellidos,
            provider=provider,
            password=settings.SOCIAL_AUTH_PASSWORD,
        )
        user = iniciarSesion(email=email, password=settings.SOCIAL_AUTH_PASSWORD)
        return user
