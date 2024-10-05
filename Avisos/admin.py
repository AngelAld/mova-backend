from django.contrib import admin
from .models import Aviso, EstadoAviso, Favorito, TipoOperacion, Alerta

admin.site.register(Aviso)
admin.site.register(EstadoAviso)
admin.site.register(Favorito)
admin.site.register(TipoOperacion)
admin.site.register(Alerta)
