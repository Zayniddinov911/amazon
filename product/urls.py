from django.urls import path
from .views import HomeView, ProductView, ProductDetailView

app_name = 'products'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductView.as_view(), name='product'),
    path('<int:pk>/details/', ProductDetailView.as_view(), name='details'),
]


