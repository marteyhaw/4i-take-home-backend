from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    telephone = models.CharField(max_length=17, unique=True)
    bio = models.TextField(max_length=1000)
    union = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    class Meta:
        ordering = ["last_name", "first_name"]
