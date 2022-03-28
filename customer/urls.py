from django.urls import path
from .views import CreateAccountView, LoginView,  logout_view
app_name = 'acc'

urlpatterns = [
    path('registration/', CreateAccountView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/',  logout_view, name='logout'),
]