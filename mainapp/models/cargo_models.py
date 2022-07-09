from django.db import models

from mainapp.models.ship_models import TransportShip
from mainapp.models.resource_models import Resource
from mainapp.models.edge_models import LandRoute


class Cargo(models.Model):
    class Meta:
        abstract = True

    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class ShipCargo(Cargo):
    owner = models.ForeignKey(TransportShip, on_delete=models.PROTECT, related_name='cargos')

    def __str__(self):
        return f"{self.id} Cargo {self.resource.name} of {self.owner}"


class LandCargo(models.Model):
    route = models.ForeignKey(LandRoute, on_delete=models.PROTECT, related_name='cargos')
    departure = models.DateTimeField()  # возможно, стоит сделать PositiveBigIntegerField
    arrival = models.DateTimeField()

    def __str__(self):
        return f"{self.id} Cargo {self.resource.name} on {self.route}"
