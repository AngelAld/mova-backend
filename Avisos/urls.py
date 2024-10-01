from .views import AvisoLista, AvisoDetalle
from django.urls import path, include

urlpatterns = [
    path("lista/", AvisoLista.as_view(), name="aviso-lista"),
    path("detalle/<slug:slug>/", AvisoDetalle.as_view(), name="aviso-detalle"),
]
