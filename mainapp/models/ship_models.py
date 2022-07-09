from django.db import models

from mainapp.models.node_models import Node
from mainapp.models.edge_models import SeaRoute


class TransportShip(models.Model):
    SHIP_TYPES = (
        ('TS', 'Tankship'),
        ('CS', 'Container ship'),
        ('BC', 'Bulk carrier'))

    type = models.CharField(max_length=255, choices=SHIP_TYPES)
    name = models.CharField(max_length=255)
    speed = models.DecimalField(max_digits=6, decimal_places=2)
    arc_type = models.PositiveSmallIntegerField()
    load_capacity = models.PositiveIntegerField()
    current_load = models.PositiveIntegerField()

    class Navigation:
        sea_port = models.ForeignKey(Node, null=True, related_name='ships', on_delete=models.CASCADE)
        sea_route = models.ForeignKey(SeaRoute, null=True, related_name='ships', on_delete=models.CASCADE)
        departure = models.DateTimeField(null=True)
        arrival = models.DateTimeField(null=True)
