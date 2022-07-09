from django.db import models

from mainapp.models.ship_models import TransportShip
from mainapp.models.resource_models import Resource
from mainapp.models.edge_models import LandRoute
from mainapp.models.node_models import Node


class Cargo(models.Model):
    class Meta:
        abstract = True

    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class ShipCargo(Cargo):
    owner = models.ForeignKey(TransportShip, on_delete=models.CASCADE, related_name='cargos')

    def __str__(self):
        return f"{self.id} Cargo {self.resource.name} of {self.owner}"


class LandCargo(models.Model):
    route = models.ForeignKey(LandRoute, on_delete=models.CASCADE, related_name='cargos')
    departure = models.DateTimeField()  # возможно, стоит сделать PositiveBigIntegerField
    arrival = models.DateTimeField()

    def __str__(self):
        return f"{self.id} Cargo {self.resource.name} on {self.route}"


class Offer(Cargo):
    node = models.ForeignKey(Node, related_name='offers', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2)


class ContractedOffer(Cargo):
    owner = models.ForeignKey(TransportShip, related_name='contracted_offers', on_delete=models.CASCADE)
    start_node = models.ForeignKey(Node, related_name='contracted_offers_from', on_delete=models.CASCADE)
    end_node = models.ForeignKey(Node, related_name='contracted_offers_to', on_delete=models.CASCADE)
    buy_price = models.DecimalField(max_digits=12, decimal_places=2)
    sell_price = models.DecimalField(max_digits=12, decimal_places=2)
    picked = models.BooleanField(default=False)
    departure = models.DateTimeField(null=True)  # возможно, стоит сделать PositiveBigIntegerField
    arrival = models.DateTimeField(null=True)
