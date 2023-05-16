from django.shortcuts import render
from . import models
from phonenumber_field.phonenumber import PhoneNumber


def phonenumber(request, phonenumber):
    person = models.Person.objects.get(
        phone_number=PhoneNumber.from_string('+' + phonenumber))
    return render(request, 'phonenumber.html',  {"person": person})


def name(request, name):
    person = models.Person.objects.get(name=name)
    return render(request, 'name.html', {"person": person})
