from django import forms

from order.models import OrderModel


class OrderModelForm(forms.ModelForm):
    
    class Meta:
        model = OrderModel
        exclude = ['customer', 'created_at', 'total_price']