from django.core.validators import MinValueValidator
from django.db import models


class Asset(models.Model):
    asset_name = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    color = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    certification = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.asset_name} (S/N:{self.serial_number})"

    class Meta:
        ordering = ["asset_name"]
