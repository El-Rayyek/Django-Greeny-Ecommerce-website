from django.urls import path
from .views import Product_list , product_detail , Category_list , Brand_list , Brand_detail , product_list

app_name = 'products'

urlpatterns = [
    path('', Product_list.as_view(),name='product_list'),
    path('test', product_list),
    path('category/',Category_list.as_view(),name = 'category_list'),
    path('brand/',Brand_list.as_view(),name = 'brand_list'),
    path('brand/<slug:slug>/',Brand_detail.as_view(),name = 'brand_detail'),
    path('<slug:slug>/', product_detail.as_view() , name = 'product_detail'),
    

]