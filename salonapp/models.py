from django.db import models

# Create your models here.
class Salons(models.Model):
    title=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    city = models.CharField(max_length=100)
    about=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)