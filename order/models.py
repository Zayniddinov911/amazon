import email
from operator import mod
from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _
from product.models import ProductModel
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class OrderModel(models.Model):
    customer = models.ForeignKey(UserModel, on_delete=models.RESTRICT, related_name='orders', verbose_name=_('customer'))
    total_price = models.FloatField()
    product = models.ManyToManyField(ProductModel)
    
    full_name = models.CharField(max_length=150, verbose_name=_('full name'))
    email = models.EmailField(verbose_name=_('email'))
    address = models.CharField(max_length=255, verbose_name=_('address'))
    City = models.CharField(max_length=50, verbose_name=_('city'))
    Country = models.CharField(max_length=50, verbose_name=_('country'))
    zip = models.PositiveIntegerField(max_length=6, verbose_name=_('zip code'))
    name_on_card = models.CharField(max_length=70, verbose_name=_('verbose_name'))
    card_number = models.PositiveIntegerField(max_length=16, verbose_name=_('card number'))
    Exp_month = models.DecimalField(max_digits=5, decimal_places=5, verbose_name=_('expiration month'))
    exp_year = models.PositiveIntegerField(max_length=4, verbose_name=_('expiration year'))
    CVV = models.PositiveIntegerField(max_length=5, verbose_name=_('CVV'))
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'{self.full_name}'
    
    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'
            