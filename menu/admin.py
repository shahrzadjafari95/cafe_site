from django.contrib import admin
from menu.models import Menu, Category


# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category', 'status', 'created_date', 'published_date']
    list_filter = ['category', 'status', 'created_date']
