from Usuarios.models import OneTimePassword, User
from Usuarios.utils import enviarCorreoVerificacion
from .serializers import (
    RegistrarUsuarioInmobiliariaSerializer,
    RegistrarUsuarioParticularSerializer,
    IniciarSesionSerializer,
    ReestablecerContraseñaSerializer,
    CambiarContraseñaSerializer,
    CerrarSesionSerializer,
)
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import smart_str, DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class RegistrarUsuarioParticularView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegistrarUsuarioParticularSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = serializer.data
        enviarCorreoVerificacion(user["email"])
        return Response(
            {
                "message": "Usuario creado exitosamente. Se ha enviado un correo de verificación.",
                "data": user,
            },
            status=status.HTTP_201_CREATED,
        )


class RegistrarUsuarioInmobiliariaView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegistrarUsuarioInmobiliariaSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = serializer.data
        enviarCorreoVerificacion(user["email"])
        return Response(
            {
                "message": "Usuario creado exitosamente. Se ha enviado un correo de verificación.",
                "data": user,
            },
            status=status.HTTP_201_CREATED,
        )


class VerificarEmail(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        otp = request.data["otp"]
        try:
            user_otp = OneTimePassword.objects.get(code=otp)
            user = user_otp.user
            if not user == request.user:
                return Response(
                    {"message": "Código no válido."}, status=status.HTTP_400_BAD_REQUEST
                )
            if not user.is_verified:
                user.is_verified = True
                user.save()
                user_otp.delete()
                return Response(
                    {"message": "Correo verificado exitosamente."},
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"message": "El correo ya ha sido verificado."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except OneTimePassword.DoesNotExist:
            return Response(
                {"message": "Código no válido."},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ReenviarEmail(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        OneTimePassword.objects.filter(user=request.user).delete()
        enviarCorreoVerificacion(request.user.email)
        return Response(
            {"message": "Correo reenviado exitosamente."},
            status=status.HTTP_200_OK,
        )


class IniciarSesion(GenericAPIView):
    serializer_class = IniciarSesionSerializer

    def post(self, request):
        serializer = self.get_serializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReestablecerContraseñaPeticion(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = ReestablecerContraseñaSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            {
                "message": "Se ha enviado un correo electrónico con las instrucciones para reestablecer la contraseña."
            },
            status=status.HTTP_200_OK,
        )


class ReestablecerContraseñaConfirmar(GenericAPIView):
    def get(self, request, uidb64, token):
        try:
            user_id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=user_id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response(
                    {"error": "Token no válido, solicite un nuevo enlace."},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
            return Response(
                {"message": "Token válido.", "uidb64": uidb64, "token": token},
                status=status.HTTP_200_OK,
            )
        except DjangoUnicodeDecodeError:
            return Response(
                {"error": "Token no válido, solicite un nuevo enlace."},
                status=status.HTTP_401_UNAUTHORIZED,
            )


class CambiarContraseña(GenericAPIView):
    serializer_class = CambiarContraseñaSerializer

    def patch(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            {"message": "Contraseña cambiada exitosamente."},
            status=status.HTTP_200_OK,
        )


class CerrarSesion(GenericAPIView):
    serializer_class = CerrarSesionSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )
