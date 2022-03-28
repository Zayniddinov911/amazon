from django.shortcuts import render
from django.views.generic import ListView
from .models import CategoryModel, ProductModel


class HomeView(ListView):
    template_name = 'main/home.html'
    model = CategoryModel


class ProductView(ListView):
    template_name = 'main/products.html'
    model = ProductModel
