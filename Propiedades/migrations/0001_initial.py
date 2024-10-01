# Generated by Django 5.1.1 on 2024-09-28 04:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Ubicacion', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Caracteristica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubTipoPropiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoAntiguedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoPropiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Propiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habitaciones', models.PositiveIntegerField(blank=True, null=True)),
                ('baños', models.PositiveIntegerField(blank=True, null=True)),
                ('pisos', models.PositiveIntegerField(blank=True, null=True)),
                ('ascensores', models.PositiveIntegerField(blank=True, null=True)),
                ('estacionamientos', models.PositiveIntegerField(blank=True, null=True)),
                ('area_construida', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('area_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('precio_soles', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('precio_dolares', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('mantenimiento', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('años', models.PositiveIntegerField(blank=True, null=True)),
                ('caracteristicas', models.ManyToManyField(blank=True, to='Propiedades.caracteristica')),
                ('dueño', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subtipo_propiedad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Propiedades.subtipopropiedad')),
                ('tipo_antiguedad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Propiedades.tipoantiguedad')),
                ('tipo_propiedad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Propiedades.tipopropiedad')),
            ],
        ),
        migrations.CreateModel(
            name='PlanoPropiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plano', models.ImageField(upload_to='planos/')),
                ('propiedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planos', to='Propiedades.propiedad')),
            ],
        ),
        migrations.CreateModel(
            name='ImagenPropiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.PositiveIntegerField(default=0)),
                ('imagen', models.ImageField(upload_to='propiedades/')),
                ('cover', models.BooleanField(default=False)),
                ('propiedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='Propiedades.propiedad')),
            ],
        ),
        migrations.CreateModel(
            name='UbicaciónPropiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle_numero', models.CharField(max_length=100)),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
                ('distrito', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Ubicacion.distrito')),
                ('propiedad', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ubicacion', to='Propiedades.propiedad')),
            ],
        ),
    ]
