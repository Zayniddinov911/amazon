from django.urls import path
from .views import CreateAccountView, LoginView, LogoutView

app_name = 'acc'

urlpatterns = [
    path('registration/', CreateAccountView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('', LogoutView.as_view(), name='logout'),
]