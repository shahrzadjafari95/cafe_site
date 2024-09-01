from django.contrib import admin
from menu.models import Product, Category


# Register your models here.
    list_filter = ['category', 'status', 'created_date']
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'status', 'created_date', 'published_date']
    search_fields = ['price', 'content', 'name']
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
    list_filter = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Menu, MenuAdmin)
