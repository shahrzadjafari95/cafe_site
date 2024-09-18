from django.contrib import admin
from menu.models import Product, Category
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter, DropdownFilter
from rangefilter.filters import DateRangeFilter
from django_admin_filters import MultiChoice


# Register your models here.

class StatusFilter(MultiChoice):
    FILTER_LABEL = "By status"


class ProductAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['name', 'price', 'category', 'status', 'created_date', 'published_date']
    list_filter = [('category', RelatedDropdownFilter),
                   ('status', StatusFilter),
                   ('created_date', DateRangeFilter)]
    search_fields = ['price', 'content', 'name']
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
    list_filter = [('name', DropdownFilter)]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
