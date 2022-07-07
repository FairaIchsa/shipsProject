from django.db import models

from mainapp.models.node_models import Node


class Edge(models.Model):
    class Meta:
        abstract = True

    node_0 = None
    node_1 = None
    length = models.DecimalField(max_digits=10, decimal_places=2)


class SeaRoute(Edge):
    node_0 = models.ForeignKey(Node, on_delete=models.PROTECT, related_name='sea_start_for')
    node_1 = models.ForeignKey(Node, on_delete=models.PROTECT, related_name='sea_end_for')
    ice_level = models.PositiveSmallIntegerField()  # добавить validator
    fullness = models.PositiveSmallIntegerField()   # текущая заполненность
    bandwidth = models.PositiveSmallIntegerField()  # пропускная способность

    def __str__(self):
        return f"Sea route {self.id}"


class Supply(Edge):
    TYPE_CHOICES = (
        ('RW', 'Railway'),
        ('PL', 'Pipeline')
    )

    node_0 = models.ForeignKey(Node, on_delete=models.PROTECT, related_name='land_start_for')
    node_1 = models.ForeignKey(Node, on_delete=models.PROTECT, related_name='land_end_for')
    type = models.CharField(max_length=255, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.type} {self.id}"



