from django.db import models

from mainapp.models.resource_models import Resource
from mainapp.models.node_models import Node
from mainapp.models.ship_models import TransportShip


class Offer(models.Model):
    node = models.ForeignKey(Node, related_name='offers')
    resource = models.ForeignKey(Resource, related_name='offers')
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)


class ContractedOffer(models.Model):
    owner = models.ForeignKey(TransportShip, related_name='contracted_offers')
    start_node = models.ForeignKey(Node, related_name='contracted_offers_from')
    end_node = models.ForeignKey(Node, related_name='contracted_offers_to')
    resource = models.ForeignKey(Resource, related_name='contracted_offers')
    quantity = models.PositiveIntegerField()
    buy_price = models.DecimalField(max_digits=12, decimal_places=2)
    sell_price = models.DecimalField(max_digits=12, decimal_places=2)
