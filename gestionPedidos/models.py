from django.db import models

# Create your models here.

class Clients(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=7)

class Articles(models.Model):
    name = models.CharField(max_length = 30)
    section = models.CharField(max_length = 20)
    price = models.IntegerField()

class orders(models.Model):
    num = models.IntegerField()
    date_order = models.DateField()
    delivered = models.BooleanField()
