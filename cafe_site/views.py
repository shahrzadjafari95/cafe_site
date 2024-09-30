from django.contrib import messages
from django.shortcuts import render
from cafe_site.forms import ContactForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == "POST":
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')