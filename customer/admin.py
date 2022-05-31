from pyexpat import model
from re import M
from django.contrib import admin
from .models import CustomerModel


@admin.register(CustomerModel)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['username']
    list_display_links = ['username']
    search_fields = ['username']
    
    
