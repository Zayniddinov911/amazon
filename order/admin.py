from re import search
from django.contrib import admin

from order.models import OrderModel

@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'created_at']
    list_display_links = ['id', 'full_name', 'created_at']
    search_fields = ['full_name', 'created_at']
    
    
