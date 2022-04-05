from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from django.db.models import Min, Max


class HomeView(ListView):
    template_name = 'main/home.html'
    model = CategoryModel


class ProductView(ListView):
    template_name = 'main/products.html'
    model = ProductModel
    # paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductView, self, **kwargs).get_context_data()
        context['categories'] = CategoryModel.objects.all()
        context['size'] = SizeModel.objects.all()
        context['color'] = ColorModel.objects.all()

        context['min_price'], context['max_price'] = ProductModel.objects.aggregate(
            Min('discount_price'),
            Max('discount_price')).values()

        return context

    def get_queryset(self):
        qs = ProductModel.objects.all()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(name__containes=q)
            return qs

        cat = self.request.GET.get('cat')
        if cat:
            qs = qs.filter(category_id=cat)

        size = self.request.GET.get('size')
        if size:
            qs = qs.filter(size__id=size)

        color = self.request.GET.get('color')
        if color:
            qs = qs.filter(color_id=color)


class ProductDetailView(DetailView):
    template_name = 'main/product-details.html'
    model = ProductModel

    def get_queryset(self):
        pass
