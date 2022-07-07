from django.db import models


class TransportShip(models.Model):
    SHIP_TYPES = (
        ('TS', 'Tankship'),
        ('CS', 'Container ship'),
        ('BC', 'Bulk carrier'))

    type = models.CharField(max_length=255, choices=SHIP_TYPES)
    name = models.CharField(max_length=255)
