from Avisos.models import AvisoAlerta
from .views import AvisoLista, AvisoDetalle, AlertaLista, AlertaCreate, AvisoAlertaList
from django.urls import path, include

urlpatterns = [
    path("lista/", AvisoLista.as_view(), name="aviso-lista"),
    path("detalle/<slug:slug>/", AvisoDetalle.as_view(), name="aviso-detalle"),
    path("alertas/lista/", AlertaLista.as_view(), name="alerta-lista"),
    path("alertas/crear/", AlertaCreate.as_view(), name="alerta-crear"),
    path(
        "alertas/<int:pk>/avisos/", AvisoAlertaList.as_view(), name="aviso-alerta-lista"
    ),
]
