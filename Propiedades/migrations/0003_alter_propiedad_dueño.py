# Generated by Django 5.1.1 on 2024-09-28 07:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Propiedades', '0002_subtipopropiedad_tipo_propiedad'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='dueño',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propiedades', to=settings.AUTH_USER_MODEL),
        ),
    ]
