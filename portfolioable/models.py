from operator import mod
from django.db import models

class Portfolio(models.Model):
    # portfolio_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    notes = models.CharField(max_length=2000)

class Property(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=2000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    rating =  models.IntegerField()
    monthly_payment = models.IntegerField()
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)    

    # def __str__(self):
    #     return self.name 
    