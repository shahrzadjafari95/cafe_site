from django.contrib import admin
from cafe_site.models import Contact


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ['name', 'email', 'created_date']
    list_filter = ['created_date']
    search_fields = ['email', 'message', 'name']

