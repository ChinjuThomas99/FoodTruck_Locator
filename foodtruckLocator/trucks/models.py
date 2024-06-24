from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class FoodTruck(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name