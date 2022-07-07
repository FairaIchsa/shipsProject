from django.db import models


class Resource(models.Model):
    MATERIAL_TYPES = (
        ('GS', 'Gas'),  # ?
        ('LQ', 'Liquid'),
        ('CT', 'Container'),
        ('LS', 'Loose')
    )

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=MATERIAL_TYPES)
    weight = models.PositiveIntegerField()  # вес единицы товара
