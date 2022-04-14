from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


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


class BrandModel(models.Model):
    name = models.CharField(max_length=244, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'


class ProductModel(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    image = models.ImageField(upload_to='products', verbose_name=_('image'))
    price = models.FloatField(verbose_name=_('price'))
    discount_price = models.FloatField(verbose_name=_('discount price'), default=0)
    discount = models.PositiveIntegerField(default=0, verbose_name=_('discount'))
    short_description = models.TextField(verbose_name=_('short description'))
    long_description = models.TextField(verbose_name=_('long description'))
    is_active = models.BooleanField(default=True, verbose_name=_('is active'))
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.RESTRICT,
        related_name='products',
        verbose_name=_('category')
    )
    color = models.ManyToManyField(
        ColorModel,
        related_name='products',
        verbose_name=_('color')
    )
    size = models.ManyToManyField(
        SizeModel,
        related_name='products',
        verbose_name=_('size'),
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def is_new(self):
        return (timezone.now() - self.created_at).days >= 3

    def is_discount(self):
        return self.discount != 0

    # def get_related(self):
    #     return ProductModel.objects.filter()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    @staticmethod
    def get_cart_info(cart):
        return ProductModel.objects.filter(id__in=cart)



class ReviewModel(models.Model):
    product = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name=_('review')
    )
    name = models.CharField(max_length=65, verbose_name=_('name'))
    comment = models.CharField(max_length=255, verbose_name=_('comment'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    country = models.CharField(max_length=50, verbose_name=_('country'))

    class Meta:
        verbose_name = 'review'
        verbose_name_plural = 'reviews'

    def __str__(self):
        return self.name


class ProductImageModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='product_image')
    image = models.ImageField(upload_to='product_image/')

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'product image'
        verbose_name_plural = 'product images'
