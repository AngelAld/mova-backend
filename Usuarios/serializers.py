from rest_framework import serializers
from Planes.models import Plan
from .models import PerfilInmobiliaria, PerfilParticular, User
from django.db.transaction import atomic
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from django.utils.encoding import smart_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from .utils import enviarCorreo
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class PerfilParticularSerializer(serializers.ModelSerializer):
    plan = serializers.StringRelatedField(source="plan.nombre", read_only=True)

    class Meta:
        model = PerfilParticular
        fields = ["dni", "telefono", "plan"]


class RegistrarUsuarioParticularSerializer(serializers.ModelSerializer):
    contraseña = serializers.CharField(max_length=68, min_length=8, write_only=True)
    confirmar_contraseña = serializers.CharField(
        max_length=68, min_length=8, write_only=True
    )
    perfil = PerfilParticularSerializer(
        source="perfil_particular", many=False, write_only=True
    )
    access = serializers.CharField(max_length=255, read_only=True)
    refresh = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = [
            "email",
            "nombres",
            "apellidos",
            "contraseña",
            "confirmar_contraseña",
            "perfil",
            "access",
            "refresh",
        ]

    def validate(self, attrs):
        if attrs["contraseña"] != attrs["confirmar_contraseña"]:
            raise serializers.ValidationError(
                {"contraseña": "Las contraseñas no coinciden."}
            )
        return super().validate(attrs)

    @atomic
    def create(self, validated_data):
        perfil = validated_data.pop("perfil_particular", {})
        plan, _ = Plan.objects.get_or_create(
            nombre="Gratuito",
            defaults={
                "precio": 0,
                "num_propiedades": 3,
                "num_empleados": 0,
                "compartir_comision": False,
            },
        )
        try:
            user = User.objects.create(
                email=validated_data["email"],
                nombres=validated_data["nombres"],
                apellidos=validated_data["apellidos"],
            )
            user.set_password(validated_data["contraseña"])
            user.save()
            PerfilParticular.objects.create(
                usuario=user,
                dni=perfil.get("dni"),
                telefono=perfil.get("telefono"),
                plan=plan,
            )

            token = user.tokens()

            return {
                "email": user.email,
                "nombres": user.nombres,
                "apellidos": user.apellidos,
                "access": str(token["access"]),
                "refresh": str(token["refresh"]),
            }
        except Exception as e:
            raise serializers.ValidationError({"detail": str(e)})


class PerfilInmobiliariaSerializer(serializers.ModelSerializer):
    plan = serializers.StringRelatedField(source="plan.nombre", read_only=True)

    class Meta:
        model = PerfilInmobiliaria
        fields = ["razon_social", "ruc", "telefono", "plan"]


class RegistrarUsuarioInmobiliariaSerializer(serializers.ModelSerializer):
    contraseña = serializers.CharField(max_length=68, min_length=8, write_only=True)
    confirmar_contraseña = serializers.CharField(
        max_length=68, min_length=8, write_only=True
    )
    perfil = PerfilInmobiliariaSerializer(
        source="perfil_inmobiliaria", many=False, write_only=True
    )
    access = serializers.CharField(max_length=255, read_only=True)
    refresh = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = [
            "email",
            "nombres",
            "apellidos",
            "contraseña",
            "confirmar_contraseña",
            "perfil",
            "access",
            "refresh",
        ]

    def validate(self, attrs):
        if attrs["contraseña"] != attrs["confirmar_contraseña"]:
            raise serializers.ValidationError(
                {"contraseña": "Las contraseñas no coinciden."}
            )
        return super().validate(attrs)

    @atomic
    def create(self, validated_data):
        try:
            perfil = validated_data.pop("perfil_inmobiliaria")
            plan, _ = Plan.objects.get_or_create(
                nombre="Gratuito Inmobiliaria",
                defaults={
                    "precio": 0,
                    "num_propiedades": 10,
                    "num_empleados": 3,
                    "compartir_comision": True,
                },
            )
            user = User.objects.create(
                email=validated_data["email"],
                nombres=validated_data["nombres"],
                apellidos=validated_data["apellidos"],
                is_inmobiliaria=True,
            )
            user.set_password(validated_data["contraseña"])
            user.save()
            PerfilInmobiliaria.objects.create(
                usuario=user,
                razon_social=perfil["razon_social"],
                ruc=perfil["ruc"],
                telefono=perfil["telefono"],
                plan=plan,
            )

            token = user.tokens()

            return {
                "email": user.email,
                "nombres": user.nombres,
                "apellidos": user.apellidos,
                "access": str(token["access"]),
                "refresh": str(token["refresh"]),
            }
        except Exception as e:
            raise serializers.ValidationError({"detail": str(e)})


class IniciarSesionSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    contraseña = serializers.CharField(max_length=68, min_length=8, write_only=True)
    nombres = serializers.CharField(max_length=255, read_only=True)
    apellidos = serializers.CharField(max_length=255, read_only=True)
    access = serializers.CharField(max_length=255, read_only=True)
    refresh = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ["email", "contraseña", "nombres", "apellidos", "access", "refresh"]

    def validate(self, attrs):
        email = attrs.get("email")
        contraseña = attrs.get("contraseña")
        request = self.context.get("request")
        user = authenticate(request, email=email, password=contraseña)
        if not user:
            raise AuthenticationFailed("Correo electrónico o contraseña incorrectos.")
        token = user.tokens()

        return {
            "email": user.email,
            "nombres": user.nombres,
            "apellidos": user.apellidos,
            "access": str(token["access"]),
            "refresh": str(token["refresh"]),
        }


class ReestablecerContraseñaSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = ["email"]

    def validate(self, attrs):
        email = attrs.get("email")

        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                "No se encontró un usuario con ese correo electrónico."
            )
        user = User.objects.get(email=email)
        uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
        token = PasswordResetTokenGenerator().make_token(user)
        request = self.context.get("request")
        current_site = get_current_site(request=request).domain
        relative_link = reverse(
            "confirmar-reestablecer-contrasena",
            kwargs={"uidb64": uidb64, "token": token},
        )
        abslink = f"http://{current_site}{relative_link}"
        email_body = (
            f"Usa el siguiente enlace para reestablecer tu contraseña\n {abslink}"
        )
        data = {
            "email_body": email_body,
            "email_subject": "Reestablecer tu contraseña",
            "to_email": user.email,
        }
        enviarCorreo(data)

        return super().validate(attrs)


class CambiarContraseñaSerializer(serializers.Serializer):
    contraseña = serializers.CharField(max_length=68, min_length=8, write_only=True)
    confirmar_contraseña = serializers.CharField(
        max_length=68, min_length=8, write_only=True
    )
    uidb64 = serializers.CharField(write_only=True)
    token = serializers.CharField(write_only=True)

    class Meta:
        fields = ["contraseña", "confirmar_contraseña", "uidb64", "token"]

    def validate(self, attrs):
        try:
            token = attrs.get("token")
            uidb64 = attrs.get("uidb64")
            contraseña = attrs.get("contraseña")
            confirmar_contraseña = attrs.get("confirmar_contraseña")

            user_id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=user_id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed(
                    "Token no válido, solicite un nuevo enlace.", code=401
                )
            if contraseña != confirmar_contraseña:
                raise serializers.ValidationError("Las contraseñas no coinciden.")
            user.set_password(contraseña)
            user.save()

            return user
        except Exception as e:
            return AuthenticationFailed(
                "Token no válido, solicite un nuevo enlace.", code=401
            )


class CerrarSesionSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        "bad_token": "El token de actualización es inválido o ha expirado."
    }

    def validate(self, attrs):
        self.token = attrs.get("refresh")
        return attrs

    def save(self, kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail("bad_token")
