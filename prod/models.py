from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

adm_choices = (('yes','yes'),('no','no'))


class UserModel(models.Model):
    name = models.CharField(max_length=48)
    surname = models.CharField(max_length=48)
    phone = PhoneNumberField(region='RU', blank=True)
    mail = models.EmailField()
    age = models.PositiveIntegerField()
    password = models.CharField(max_length=255)
    is_admin = models.CharField(max_length=3,choices=adm_choices)
