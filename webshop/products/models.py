from django.db import models
import datetime
from django.utils import timezone


# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_description = models.CharField(max_length=10000)
    price = models.FloatField()
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to="")

    def __str__(self):
        return self.product_name
