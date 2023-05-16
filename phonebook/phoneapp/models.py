from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    phone_number = PhoneNumberField()
    addres = models.CharField(max_length=50)
