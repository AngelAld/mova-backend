from rest_framework.permissions import BasePermission

from Avisos.models import Aviso
from Usuarios.models import User
from .models import Propiedad
from Planes.models import Plan


class IsDueño(BasePermission):
    def has_object_permission(self, request, view, obj: Propiedad):
        user: User = request.user
        dueño: User = obj.dueño

        if hasattr(dueño, "perfil_inmobiliaria"):
            return user == dueño
        if hasattr(dueño, "perfil_particular"):
            return user == dueño
        if hasattr(dueño, "perfil_empleado"):
            return user == dueño or user == dueño.inmobiliaria.dueño


class IsDueñoAviso(BasePermission):
    def has_object_permission(self, request, view, obj: Aviso):
        return obj.propiedad.dueño == request.user


class maxPropiedades(BasePermission):
    def has_permission(self, request, view):
        if request.method != "POST":
            return True

        user: User = request.user
        if hasattr(user, "perfil_particular"):
            return (
                user.perfil_particular.plan.num_propiedades >= user.propiedades.count()
            )

        if hasattr(user, "perfil_inmobiliaria") and user.is_inmobiliaria:
            return (
                user.perfil_inmobiliaria.plan.num_propiedades
                >= user.propiedades.count()
            )

        if hasattr(user, "perfil_empleado"):
            return (
                user.perfil_empleado.inmobiliaria.plan.num_propiedades
                >= user.propiedades.count()
            )
        return False
