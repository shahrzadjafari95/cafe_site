from django.contrib import admin
from menu.models import Product, Category
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter, DropdownFilter


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'status', 'created_date', 'published_date']
    list_filter = [('category', RelatedDropdownFilter),
    search_fields = ['price', 'content', 'name']
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
    list_filter = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Menu, MenuAdmin)
