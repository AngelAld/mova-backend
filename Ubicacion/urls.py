from django.urls import path
from .views import DepartamentoListView, ProvinciaListView, DistritoListView

urlpatterns = [
    path(
        "departamento/lista/", DepartamentoListView.as_view(), name="departamento-list"
    ),
    path("provincia/lista/", ProvinciaListView.as_view(), name="provincia-list"),
    path("distrito/lista/", DistritoListView.as_view(), name="distrito-list"),
]
