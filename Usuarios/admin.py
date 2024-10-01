from django.contrib import admin
from .models import (
    User,
    OneTimePassword,
    PerfilInmobiliaria,
    PerfilParticular,
    PerfilEmpleado,
)


admin.site.register(User)
admin.site.register(OneTimePassword)
admin.site.register(PerfilInmobiliaria)
admin.site.register(PerfilParticular)
admin.site.register(PerfilEmpleado)
