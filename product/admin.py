from django.contrib import admin
from .models import *


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    list_display_links = ['id', 'name']
    search_fields = ['name']

