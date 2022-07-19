from django.db import models


class Node(models.Model):
    NODE_TYPES = (
        ('SN', 'Sea Node'),
        ('SP', 'Seaport'),
        ('LN', 'Land Node'),
        ('LH', 'Land Hub'),
    )

    name = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, choices=NODE_TYPES)

    coord_x = models.DecimalField(max_digits=5, decimal_places=2)
    coord_y = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"
