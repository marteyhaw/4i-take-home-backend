from django.core.validators import RegexValidator
from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    telephone_regex = RegexValidator(
        regex=r"^(\+\d{1,2}\s?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$",
        message="Examples: 123-456-7890, (123) 456-7890, 123 456 7890, 123.456.7890, +91 (123) 456-7890",
    )
    telephone = models.CharField(validators=[telephone_regex], max_length=17)
    bio = models.TextField()
    union = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    class Meta:
        ordering = ["last_name", "first_name"]
