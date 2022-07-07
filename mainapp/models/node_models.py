from django.db import models


class Node(models.Model):
    name = models.CharField(max_length=255)

    coord_x = models.DecimalField(max_length=7, max_digits=2)
    coord_y = models.DecimalField(max_length=7, max_digits=2)

    available_cargo = None
    requested_cargo = None
    contracted_cargo = None

    def deliver_from(self):
        pass

    def deliver_to(self):
        pass