from django.db import models


class Resource(models.Model):
    MATERIAL_TYPES = (
        ('GS', 'Gas'),  # ?
        ('LQ', 'Liquid'),
        ('CT', 'Container'),  # нужно прикрутить механику для контейнеров разных размеров
        ('LS', 'Loose')
    )

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=MATERIAL_TYPES)
