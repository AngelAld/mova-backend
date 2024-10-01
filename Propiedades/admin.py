from django.contrib import admin
from .models import (
    Caracteristica,
    TipoPropiedad,
    SubTipoPropiedad,
    TipoAntiguedad,
    Propiedad,
    ImagenPropiedad,
    PlanoPropiedad,
    UbicacionPropiedad,
)

admin.site.register(Caracteristica)
admin.site.register(TipoPropiedad)
admin.site.register(SubTipoPropiedad)
admin.site.register(TipoAntiguedad)
admin.site.register(Propiedad)
admin.site.register(ImagenPropiedad)
admin.site.register(PlanoPropiedad)
admin.site.register(UbicacionPropiedad)
