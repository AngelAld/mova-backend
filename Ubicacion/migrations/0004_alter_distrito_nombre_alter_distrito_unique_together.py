# Generated by Django 5.1.1 on 2024-10-26 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ubicacion', '0003_alter_departamento_nombre_alter_distrito_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distrito',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='distrito',
            unique_together={('nombre', 'provincia')},
        ),
    ]
