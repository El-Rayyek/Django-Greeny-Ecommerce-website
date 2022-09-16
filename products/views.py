from django.shortcuts import render
from .models import Product , ProductImage , Review , Category , Brand 
from django.views.generic import ListView , DetailView
from django.db.models import Count
# Create your views here.


class product_list(ListView):
    model = Product
    paginate_by = 1

class product_detail(DetailView):
    model = Product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        myproduct = self.get_object()
        context["images"] = ProductImage.objects.filter(product = myproduct) 
        context["reviews"] = Review.objects.filter(product = myproduct)
        return context
    
class Category_list(ListView):
    model = Category
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all().annotate(category_count = Count('product_category'))
        return context
    

class Brand_list(ListView):
    model = Brand
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brands"] = Brand.objects.all().annotate(brand_count=Count('product_brand'))
        return context
    