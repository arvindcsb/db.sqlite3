from django.db import models
from customerapp.models import Customer,Booking,Rating
from salonapp.models import Salons

# Create your models here.
class Admins(models.Model):
    fullname=models.CharField(max_length=100)
    password=models.CharField(max_length=100)