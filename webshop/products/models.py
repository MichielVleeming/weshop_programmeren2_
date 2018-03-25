from django.db import models
import datetime
from django.utils import timezone


# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_description = models.CharField(max_length=200)
    price = models.FloatField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.product_name



class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="", blank=True)
    image_description = models.CharField(max_length=200)

    def __str__(self):
        return self.image_description
