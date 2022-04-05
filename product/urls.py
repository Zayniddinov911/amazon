from django.urls import path
from .views import HomeView, ProductView, DetailView

app_name = 'products'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductView.as_view(), name='product'),
    path('details/', DetailView.as_view(), name='details')
]


