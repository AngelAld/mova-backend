from math import e
from rest_framework import serializers
from .utils import Google, registrarUsuarioGoogle
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed


class GoogleIniciarSesionSerializer(serializers.Serializer):
    access_token = serializers.CharField()

    def validate_access_token(self, access_token):
        google_user_data = Google.validar(access_token)
        try:
            user_id = google_user_data["sub"]
        except:
            raise AuthenticationFailed("Token de Google inválido")
        if google_user_data["aud"] != settings.GOOGLE_CLIENT_ID:
            raise AuthenticationFailed("Token de Google inválido")

        email = google_user_data["email"]
        nombres = google_user_data["given_name"]
        apellidos = google_user_data["family_name"]
        provider = "google"
        return registrarUsuarioGoogle(provider, email, nombres, apellidos)
