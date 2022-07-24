from django.db import models

from mainapp.models.port_models import Port


class Ship(models.Model):
    navigation = models.OneToOneField('Navigation', on_delete=models.CASCADE, related_name='ship')
    engine = models.OneToOneField('Engine', on_delete=models.CASCADE, related_name='ship')
    behavior = models.OneToOneField('Behavior', on_delete=models.CASCADE, related_name='ship')


class Navigation(models.Model):
    port = models.ForeignKey(Port, null=True, related_name='ships', on_delete=models.CASCADE)
    port_from = models.ForeignKey(Port, null=True, related_name='ships_from', on_delete=models.CASCADE)
    port_to = models.ForeignKey(Port, null=True, related_name='ships_to', on_delete=models.CASCADE)
    current_tile = models.IntegerField(default=0)


class Engine(models.Model):
    max_speed = models.PositiveIntegerField()
    average_speed = models.PositiveIntegerField()
    caravan_speed = models.PositiveIntegerField(null=True)
    is_working = models.BooleanField()


class Behavior(models.Model):
    state = models.CharField(max_length=255)
