# Generated by Django 5.1.1 on 2024-09-28 07:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Propiedades', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtipopropiedad',
            name='tipo_propiedad',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Propiedades.tipopropiedad'),
            preserve_default=False,
        ),
    ]
