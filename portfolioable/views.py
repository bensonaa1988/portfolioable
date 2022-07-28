from django.http import JsonResponse
from .models import Portfolio
from .serializers import PortfolioableSerializer


def portfolio_list(request):
    portfolios = Portfolio.objects.all()
    serializer = PortfolioableSerializer(portfolios, many=True)
    return JsonResponse(serializer.data, safe=False)