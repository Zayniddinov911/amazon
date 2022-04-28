from re import search
from django.contrib import admin

from order.models import OrderModel

@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'created_at']
    list_display_links = ['id', 'customer', 'created_at']
    search_fields = ['customer', 'created_at']
    
    
