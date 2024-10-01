from ast import Sub
import random
from django.core.mail import EmailMessage
from .models import OneTimePassword, User
from django.conf import settings


def generarOtp():
    otp = ""
    for i in range(6):
        otp += str(random.randint(0, 9))
    return otp


def enviarCorreoVerificacion(email):
    Subject = "Código de verificación"
    otp_code = generarOtp()
    print(otp_code)
    user = User.objects.get(email=email)
    current_site = "myAuth.com"
    email_body = f"Hola, {user.nombres}. Gracias por registrarte en {current_site}. Por favor, verifica tu correo electrónico con el siguiente código:\n {otp_code}"
    from_email = settings.EMAIL_HOST_USER

    OneTimePassword.objects.create(user=user, code=otp_code)

    email = EmailMessage(Subject, email_body, from_email, [email])
    email.send(fail_silently=True)


def enviarCorreo(data):
    email = EmailMessage(
        data["email_subject"],
        data["email_body"],
        settings.EMAIL_HOST_USER,
        [data["to_email"]],
    )
    email.send(fail_silently=True)
