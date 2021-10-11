from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CustomerProfile(models.Model):
    user      = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    username  = models.CharField(max_length=25)  
    first_name= models.CharField(max_length=25)
    last_name = models.CharField(max_length=25) 
    email     = models.EmailField() 
    number    = models.CharField(max_length=15)  
    address   = models.CharField(max_length=50)  
    profile_pic = models.ImageField(upload_to='media') 

    def __str__(self):
        return self.username


class Bus(models.Model):
    bus_name        = models.CharField(max_length=30)
    source          = models.CharField(max_length=30)
    destination     = models.CharField(max_length=30)
    total_seats     = models.DecimalField(decimal_places=0, max_digits=2)
    remaining_seats = models.DecimalField(decimal_places=0, max_digits=2)
    price           = models.DecimalField(decimal_places=2, max_digits=6)
    date            = models.DateField()
    time            = models.TimeField()
    bus_image       = models.ImageField(upload_to = 'media')

    def __str__(self):
        return self.bus_name
        