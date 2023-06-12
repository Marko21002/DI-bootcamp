from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Forecaster(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='forecaster')

class Report(models.Model):
    
    TYPE_CHOICES = (
        ('sunny', 'Sunny'),
        ('cloudy', 'Cloudy'),
        ('windy', 'Windy'),
        ('rainy', 'Rainy'),
        ('stormy', 'Stormy'),
    )
    
    location = models.CharField(max_length=100)
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, null=True)
    forecaster = models.ForeignKey(Forecaster,on_delete=models.CASCADE, null=True)
    
    def __str__(self) -> str:
        return f"{self.location}:{self.temperature}"
    

    
