from django.urls import path

from order.views import CheckoutView, OrderHistoryView

app_name = 'order'

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('history', OrderHistoryView.as_view(), name='history')
]
