from django.db import models

from mainapp.models.resource_models import Resource
from mainapp.models.ship_models import Ship
from mainapp.models.port_models import Port, LoadingSection


class Cargo(models.Model):
    type = models.ForeignKey(Resource, related_name='cargos', on_delete=models.CASCADE)
    weight = models.PositiveIntegerField()
    board_cargo = models.OneToOneField('BoardCargo', related_name='cargo', null=True, on_delete=models.CASCADE)
    port = models.ForeignKey(LoadingSection, related_name='cargos', null=True, on_delete=models.CASCADE)


class BoardCargo(models.Model):
    # ship = models.ForeignKey(Ship, related_name='cargos', on_delete=models.CASCADE)
    fraght = models.ForeignKey('Fraght', related_name='cargos', on_delete=models.CASCADE)
    is_loaded = models.BooleanField()
    deadweight = models.DecimalField(max_digits=12, decimal_places=2)


class Fraght(models.Model):
    ship = models.ForeignKey(Ship, related_name='fraghts', on_delete=models.CASCADE)
    is_taken = models.BooleanField()
    is_completed = models.BooleanField()
    port_from = models.ForeignKey(Port, related_name='fraght_from', on_delete=models.CASCADE)
    port_to = models.ForeignKey(Port, related_name='fraght_to', on_delete=models.CASCADE)
