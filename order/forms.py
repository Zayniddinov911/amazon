from dataclasses import field
from django import forms

from order.models import OrderModel


class OrderModelForm(forms.ModelForm):
    
    class Meta:
        model = OrderModel
        exclude = ['customer', 'created_at', 'total_price']
     
        
class OrderHistoryModelForm(forms.ModelForm):
    
    class Meta:
        model = OrderModel
        exclude = ['CVV', 
                   'exp_year', 
                   'Exp_month', 
                   'card_number', 
                   'name_on_card', 
                   'Country',
                   'zip',
                   'City',
                    "address",
                    'email',
                    'full_name',
                    'customer']
        

