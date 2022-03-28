from django.db import models
from django.utils.translation import gettext_lazy as _


class CategoryModel(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name'))
    image = models.ImageField(upload_to='category_img', verbose_name=_('image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class SizeModel(models.Model):
    name = models.CharField(max_length=7, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'size'
        verbose_name_plural = 'sizes'


class ColorModel(models.Model):
    code = models.CharField(max_length=7, verbose_name=_('code'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'


class ProductModel(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    image = models.ImageField(upload_to='products', verbose_name=_('image'))
    price = models.FloatField(verbose_name=_('price'))
    discount_price = models.FloatField(verbose_name=_('discount price'), default=0)
    discount = models.PositiveIntegerField(default=0, verbose_name=_('discount'))
    short_description = models.TextField(verbose_name=_('short description'))
    long_description = models.TextField(verbose_name=_('long description'))
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.RESTRICT,
        related_name='products',
        verbose_name=_('category')
    )
