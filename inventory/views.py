from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import Product

@require_GET
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

    # Serialize the filtered queryset to JSON
    products = [{'name': product.name,
                 'description': product.description,
                 'price': str(product.price),
                 'quantity': product.quantity,
                 'category': product.category} for product in queryset]

    return JsonResponse({'products': products})
