from django.db import models


# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    password = models.CharField(max_length=2000)

    def __str__(self):
        return self.first_name


