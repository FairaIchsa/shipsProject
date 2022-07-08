from django.db import models

from mainapp.models.ship_models import TransportShip
from mainapp.models.resource_models import Resource


class Cargo(models.Model):
    owner = models.ForeignKey(TransportShip, on_delete=models.PROTECT, related_name='cargos')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.id} Cargo {self.resource.name} of {self.owner}"
