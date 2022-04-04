from modeltranslation.translator import register, TranslationOptions
from .models import ProductModel


@register(ProductModel)
class NewsTranslationOption(TranslationOptions):
    fields = ['name', 'short_description', 'long_description']
