from django.db import models

from mainapp.models.node_models import Node


class Edge(models.Model):
    class Meta:
        abstract = True

    node_0 = models.ForeignKey(Node, on_delete=models.PROTECT)
    node_1 = models.ForeignKey(Node, on_delete=models.PROTECT)
    length = models.DecimalField(max_length=10, max_digits=2)


class SeaRoute(Edge):
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

    type = models.CharField(max_length=255, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.type} {self.id}"



