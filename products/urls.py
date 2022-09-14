from django.urls import path
from .views import product_list , product_detail

app_name = 'products'

urlpatterns = [
    path('', product_list.as_view(),name='product_list'),
    path('<int:pk>/',product_detail.as_view(),name='product_detail')
]