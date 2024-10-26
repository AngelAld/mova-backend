from django.core.management.base import BaseCommand, CommandError
from ...models import Departamento, Provincia, Distrito
import csv


class Command(BaseCommand):
    help = "Carga todos los datos de los departamentos, provincias y distritos"

    def handle(self, *args, **options):
        # Carga de departamentos
        with open(
            "Ubicacion\\management\\commands\\Ubicacion.csv", encoding="utf-8"
        ) as csvfile:
            self.stdout.write(
                self.style.SUCCESS("Cargando departamentos, provincias y distritos...")
            )
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    departamento, created = Departamento.objects.get_or_create(
                        nombre=row["Departamento"]
                    )
                    if created:
                        self.stdout.write(
                            self.style.SUCCESS(f"Departamento {departamento} creado")
                        )
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f"Error creando departamento: {e}")
                    )

                try:
                    provincia, created = Provincia.objects.get_or_create(
                        nombre=row["Provincia"], departamento=departamento
                    )
                    if created:
                        self.stdout.write(
                            self.style.SUCCESS(f"Provincia {provincia} creada")
                        )
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error creando provincia: {e}"))

                try:
                    distrito, created = Distrito.objects.get_or_create(
                        nombre=row["Distrito"], provincia=provincia
                    )
                    if created:
                        self.stdout.write(
                            self.style.SUCCESS(f"Distrito {distrito} creado")
                        )
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f"Error creando distrito: {e} on {row}")
                    )
