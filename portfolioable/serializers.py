from dataclasses import fields
from rest_framework import serializers
from .models import Portfolio


class PortfolioableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['id', 'name', 'notes']