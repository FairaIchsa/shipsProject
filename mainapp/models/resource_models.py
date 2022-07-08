from django.db import models


class Resource(models.Model):
    MATERIAL_TYPES = (
        ('GS', 'Gas'),  # 1000 кубических метров
        ('LQ', 'Liquid'),  # ?
        ('CT', 'Container'),  # 1 контейнер
        ('LS', 'Loose')  # 500 тонн
    )

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=MATERIAL_TYPES)

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"
