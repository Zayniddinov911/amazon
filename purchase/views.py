from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# from real_amazon.product.models import ProductModel
from django.views.generic import ListView

from product.models import ProductModel


def update_cart(request, pk):
    product = get_object_or_404(ProductModel.objects.all().filter(id=pk))
    cart = request.session.get('cart', [])
    if pk in cart:
        cart.remove(pk)
    else:
        cart.append(pk)

    request.session['cart'] = cart

    return redirect(request.GET.get('next', '/'))


class CartListView(ListView):
    template_name = 'main/shopping_cart.html'

    def get_queryset(self):
        cart = self.request.session.get('cart', [])
        return ProductModel.get_cart_info(cart)

