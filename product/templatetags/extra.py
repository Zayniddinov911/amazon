from django import template

from django.db.models import Sum

# from real_amazon.product.models import ProductModel

register = template.Library()


@register.filter
def is_cart(request, product):
    return product.pk in request.session.get('cart', [])
