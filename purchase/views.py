from django.shortcuts import render, redirect, get_object_or_404
from .models import WishlistModel
from django.contrib.auth.decorators import login_required
from real_amazon.product.models import ProductModel
from django.views.generic import ListView


class WishlistView(ListView):
    template_name = 'main/wishlist.html'

    def get_queryset(self):
        return ProductModel.objects.all().filter(wishlist__user_id=self.request.user)


@login_required
def update_wishlist(request, pk):
    product = get_object_or_404(ProductModel.objects.all().filter(id=pk))
    wishlist = WishlistView.add_to_delete(request)
