import re
from rest_framework.permissions import BasePermission
from Usuarios.models import PerfilEmpleado, User, PerfilInmobiliaria
from Planes.models import Plan


class IsOwnerInmobiliaria(BasePermission):
    def has_object_permission(self, request, view, obj: User):
        if request.method == "POST":
            return True
        if not hasattr(obj, "perfil_empleado"):
            return False
        if not hasattr(request.user, "perfil_inmobiliaria"):
            return False
        if obj.perfil_empleado.inmobiliaria != request.user.perfil_inmobiliaria:
            return False
        return True


class maxEmpleadosPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method != "POST":
            return True
        user: User = request.user
        if hasattr(user, "perfil_inmobiliaria"):
            return (
                user.perfil_inmobiliaria.plan.num_empleados
                >= user.perfil_inmobiliaria.empleados.count()
            )

        return False
