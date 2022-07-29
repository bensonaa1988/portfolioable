
from .models import Portfolio
from .models import Property
from .serializers import PortfolioableSerializer, PropertySerializer
from rest_framework import viewsets, permissions

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioableSerializer
    permission_classes = [permissions.AllowAny]
    
class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.AllowAny]    
    # func w/i class for update and delete 






