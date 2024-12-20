"""
URL configuration for Api project.

"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("admin/", admin.site.urls),
    path("auth/", include("Usuarios.urls")),
    path("propiedades/", include("Propiedades.urls")),
    path("avisos/", include("Avisos.urls")),
    path("ubicacion/", include("Ubicacion.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
