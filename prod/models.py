from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=64)
    picture = models.FileField()
    price = models.PositiveIntegerField()

    
class Questions(models.Model):
    user = models.CharField(max_length=32)
    question = models.CharField(max_length=52)
    answer = models.CharField(max_length=64)