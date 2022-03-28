from django.urls import path
from .views import HomeView, ProductView

app_name = 'products'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductView.as_view(), name='product'),
]


