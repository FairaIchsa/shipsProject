from django.db import models

from mainapp.models.ship_models import TransportShip


class Cargo(models.Model):
    owner = models.ForeignKey(TransportShip, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()

