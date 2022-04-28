from distutils.log import Log
from multiprocessing import context
from re import L
from django.shortcuts import render, redirect
from django.db.models import Sum
from django.urls import reverse
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from order.forms import OrderModelForm
from product.models import ProductModel
from order.models import OrderModel


class CheckoutView(LoginRequiredMixin, CreateView):
    template_name = 'main/checkout.html'
    form_class = OrderModelForm

    def get_success_url(self):
        return reverse('order:history')

    def form_valid(self, form):
        cart = self.request.session.get('cart', [])
        product = ProductModel.get_cart_info(cart)

        form.instance.customer = self.request.customer
        # form.instance.price = product.aggregate(
        #     Sum('')
        # )

        order = form.save()

        order.product.set(product)

        self.request.session['cart'] = []

        return redirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.request.session.get('cart', [])
        context['product'] = ProductModel.get_cart_info(cart)
        
        if hasattr(self.request.user, 'customer'):
            context['customer'] = self.request.user.customer

        return context


class OrderHistoryView(LoginRequiredMixin, ListView):
    template_name = 'main/o_history.html'

    def get_queryset(self):
        return self.request.user.orders.all()
