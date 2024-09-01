from django.db.models import Prefetch
from django.shortcuts import render
from django.utils import timezone
from .models import Product, Category


# Create your views here.

def index(request):
    return render(request, 'menu/menu.html')
    # Fetch categories and prefetch their products, filter products based on status and published_date
    categories = Category.objects.prefetch_related(Prefetch('products', queryset=Product.objects.
        filter(status__in=('coming_soon', 'available'), published_date__lte=timezone.now()).order_by('name'))).order_by(
        'name')
    # Filter out categories that don't have any available products
    categories_with_products = [category for category in categories if category.products.exists()]
