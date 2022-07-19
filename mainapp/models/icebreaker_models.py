from django.db import models

from mainapp.models.node_models import Node
from mainapp.models.edge_models import SeaRoute


class Icebreaker(models.Model):
    name = models.CharField(max_length=255)
    speed = models.DecimalField(max_digits=6, decimal_places=2)

    sea_port = models.ForeignKey(Node, null=True, related_name='icebreakers', on_delete=models.CASCADE)
    sea_route = models.ForeignKey(SeaRoute, null=True, related_name='icebreakers', on_delete=models.CASCADE)
    departure = models.DateTimeField(null=True)
    arrival = models.DateTimeField(null=True)
