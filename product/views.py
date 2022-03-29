from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class HomeView(ListView):
    template_name = 'main/home.html'
    model = CategoryModel


class ProductView(ListView):
    template_name = 'main/products.html'
    model = ProductModel
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductView, self, **kwargs).get_context_data()
        context['categories'] = CategoryModel.objects.all()
        context['size'] = SizeModel.objects.all()
        context['color'] = ColorModel.objects.all()
