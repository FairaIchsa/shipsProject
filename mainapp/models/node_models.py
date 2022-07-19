from django.db import models


class Node(models.Model):
    NODE_TYPES = (
        ('SN', 'Sea Node'),
        ('SP', 'Seaport'),
        ('LN', 'Land Node'),
        ('LH', 'Land Hub'),     # возможно, не будет использован
    )

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=NODE_TYPES)
    coordinates = models.CharField(max_length=255)
    # country = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"

    def is_on_water(self):
        return self.type == 'SN' or self.type == 'SP'

    def is_hub(self):
        return self.type == 'SP' or self.type == 'LH'
