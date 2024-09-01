from django.shortcuts import render
from .models import Product, Category


# Create your views here.

def index(request):
    return render(request, 'menu/menu.html')
