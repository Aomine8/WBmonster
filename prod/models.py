from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


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

adm_choices = (('yes','yes'),('no','no'))


class UserModel(models.Model):
    name = models.CharField(max_length=48)
    surname = models.CharField(max_length=48)
    phone = PhoneNumberField(region='RU', blank=True)
    mail = models.EmailField()
    age = models.PositiveIntegerField()
    password = models.CharField(max_length=255)
    is_admin = models.CharField(max_length=3,choices=adm_choices)

