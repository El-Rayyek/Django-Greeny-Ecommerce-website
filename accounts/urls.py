from django.urls import path
from .views import signup , active_user

app_name = 'accounts'

urlpatterns = [
    path('signup/',signup , name = 'signup'),
    path('<str:username>/activate',active_user , name = 'active_user'),
    
    ]