# Generated by Django 5.1.1 on 2024-09-27 02:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Planes', '0001_initial'),
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilInmobiliaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=255)),
                ('ruc', models.CharField(max_length=11, unique=True)),
                ('telefono', models.CharField(max_length=9)),
                ('aprobada', models.BooleanField(default=False)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Planes.plan')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil_inmobiliaria', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PerfilEmpleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=8, unique=True)),
                ('telefono', models.CharField(max_length=9)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil_empleado', to=settings.AUTH_USER_MODEL)),
                ('inmobiliaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empleados', to='Usuarios.perfilinmobiliaria')),
            ],
        ),
        migrations.CreateModel(
            name='PerfilParticular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=8, unique=True)),
                ('telefono', models.CharField(max_length=9)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Planes.plan')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil_particular', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
