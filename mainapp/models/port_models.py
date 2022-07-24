from django.db import models


class Port(models.Model):
    name = models.CharField(max_length=255)
    coordinates = models.CharField(max_length=255)
    max_size = models.PositiveIntegerField()
    loading_size = models.PositiveIntegerField()
