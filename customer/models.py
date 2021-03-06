from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomerModel(AbstractUser):
    email = models.EmailField(verbose_name=_('email'))
    phone = models.CharField(max_length=13, verbose_name=_('phone'))
    address = models.CharField(max_length=255, verbose_name=_('address'))
    zip_code = models.PositiveIntegerField(default=True, verbose_name=_('zip code'))
    card = models.PositiveIntegerField(default=True, verbose_name=_('Bank Card'))

    def __str__(self):
        return f'{self.username} {self.email}'
    
    class Meta:
        verbose_name = 'customer'
        verbose_name_plural = 'customers'

