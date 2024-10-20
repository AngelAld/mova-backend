# Generated by Django 5.1.1 on 2024-10-05 21:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Avisos', '0004_alter_aviso_propiedad'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alerta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propiedad_precio_soles_min', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('propiedad_precio_soles_max', models.DecimalField(decimal_places=2, default=1000000, max_digits=12)),
                ('propiedad_precio_dolares_min', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('propiedad_precio_dolares_max', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('propiedad_habitaciones_min', models.IntegerField(blank=True, null=True)),
                ('propiedad_habitaciones_max', models.IntegerField(blank=True, null=True)),
                ('propiedad_banos_min', models.IntegerField(blank=True, null=True)),
                ('propiedad_banos_max', models.IntegerField(blank=True, null=True)),
                ('propiedad_ascensores_min', models.IntegerField(blank=True, null=True)),
                ('propiedad_ascensores_max', models.IntegerField(blank=True, null=True)),
                ('propiedad_pisos_min', models.IntegerField(blank=True, null=True)),
                ('propiedad_pisos_max', models.IntegerField(blank=True, null=True)),
                ('propiedad_estacionamientos_min', models.IntegerField(blank=True, null=True)),
                ('propiedad_estacionamientos_max', models.IntegerField(blank=True, null=True)),
                ('propiedad_area_total_min', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('propiedad_area_total_max', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('propiedad_area_construida_min', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('propiedad_area_construida_max', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('propiedad_mantenimiento_min', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('propiedad_mantenimiento_max', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('propiedad_tipo_antiguedad', models.CharField(blank=True, max_length=50, null=True)),
                ('propiedad_subtipo_propiedad', models.CharField(blank=True, max_length=50, null=True)),
                ('propiedad_tipo_propiedad', models.CharField(blank=True, max_length=50, null=True)),
                ('propiedad_ubicacion_distrito', models.CharField(blank=True, max_length=50, null=True)),
                ('propiedad_ubicacion_distrito_provincia', models.CharField(blank=True, max_length=50, null=True)),
                ('propiedad_ubicacion_distrito_provincia_departamento', models.CharField(blank=True, max_length=50, null=True)),
                ('propiedad_caracteristicas', models.JSONField(blank=True, default=list)),
                ('tipo_operacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Avisos.tipooperacion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alertas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AvisoAlerta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alerta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avisos', to='Avisos.alerta')),
                ('aviso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alertas', to='Avisos.aviso')),
            ],
        ),
    ]
