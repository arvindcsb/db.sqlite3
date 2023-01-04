from django.db import models
from salonapp.models import Salons

# Create your models here.
class Contact(models.Model):
    message=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=100)

class Customer(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    city=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)

class Booking(models.Model):
    title=models.CharField(max_length=100)
    customer_email=models.EmailField(max_length=100)
    service=models.CharField(max_length=100)
    date=models.DateField()
    time=models.TimeField()
    description=models.CharField(max_length=100)

class Rating(models.Model):
    email=models.EmailField(max_length=100)
    customer_email=models.EmailField(max_length=100)
    rating=models.BigIntegerField()
    review=models.CharField(max_length=100)
    time=models.TimeField()
    date=models.DateField()
