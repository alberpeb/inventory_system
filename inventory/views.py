from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def list_products(request):
    # Get query parameters from the request
    name = request.GET.get('name', '')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    category = request.GET.get('category', '')

    # Create a base queryset
    queryset = Product.objects.all()

    # Apply filters based on query parameters
    if name:
        queryset = queryset.filter(name__icontains=name)
    if min_price:
        queryset = queryset.filter(price__gte=min_price)
    if max_price:
        queryset = queryset.filter(price__lte=max_price)
    if category:
        queryset = queryset.filter(category=category)

    serializer = ProductSerializer(queryset, many=True)

    return Response({'products': serializer.data})
