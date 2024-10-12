from posixpath import basename
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    PropiedadTiposViewSet,
    PropiedadListView,
    TipoPropiedadListView,
    SubTipoPropiedadListView,
    TipoOperacionListView,
    PropiedadDatosViewSet,
    CaracteristicaListView,
    EliminarPropiedadView,
    TipoAntiguedadListView,
    ImagenesPropiedadViewSet,
)

router = DefaultRouter()
router.register(r"tipos", PropiedadTiposViewSet, basename="tipos")
router.register(r"datos", PropiedadDatosViewSet, basename="datos")
router.register(r"imagenes", ImagenesPropiedadViewSet, basename="imagenes")

urlpatterns = [
    path("", include(router.urls)),
    path("<int:pk>/", EliminarPropiedadView.as_view(), name="eliminar"),
    path("lista/", PropiedadListView.as_view(), name="propiedades-list"),
    path("lista/tipos/", TipoPropiedadListView.as_view(), name="tipos-list"),
    path("lista/subtipos/", SubTipoPropiedadListView.as_view(), name="subtipos-list"),
    path(
        "lista/operaciones/", TipoOperacionListView.as_view(), name="operaciones-list"
    ),
    path(
        "lista/caracteristicas/",
        CaracteristicaListView.as_view(),
        name="caracteristicas-list",
    ),
    path(
        "lista/tipo-antiguedad/",
        TipoAntiguedadListView.as_view(),
        name="caracteristicas-list",
    ),
]
