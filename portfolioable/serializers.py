from dataclasses import fields
from rest_framework import serializers
from .models import Portfolio
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['portfolio','id', 'address', 'city', 'state', 'bedrooms', 'baths', 'rating', 'monthly_payment']


class PortfolioableSerializer(serializers.ModelSerializer):
    properties = PropertySerializer(many=True, required=True)
    class Meta:
        model = Portfolio
        fields = ['id', 'name', 'notes', 'properties']

# class Portfolio(models.Model):
#     name = models.CharField(max_length=200)
#     notes = models.CharField(max_length=2000)        
