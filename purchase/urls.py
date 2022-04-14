from django.urls import path
from .views import update_cart, CartListView

app_name = 'product'

urlpatterns = [
    path('<int:pk>/cart/', update_cart, name='add_cart'),
    path('shopping/cart/', CartListView.as_view(), name='shop_cart')
]