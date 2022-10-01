from django.shortcuts import render
from .models import Product , ProductImage , Review , Category , Brand 
from django.views.generic import ListView , DetailView
from django.db.models import Count
from django.db.models import Q ,F
# Create your views here.


def product_list(request):
    # querset = Product.objects.filter(name__contains='fo',price__gt = 30)
    # querset = Product.objects.filter(
    #     Q(name__contains='fo') & 
    #     ~Q(price__gt = 30))
    # queryset = Product.objects.filter(id = F('category__id'))
    # queryset = Product.objects.order_by('name','-price').reverse()
    # queryset = Product.objects.latest('name') or .earliest()
    # queryset = Product.objects.order_by('name')[10:20]
    # queryset = Product.objects.values_list('id','name','price','category__name').distinct()
    # queryset = Product.objects.only('id','name','price')
    # queryset = Product.objects.defer('id','name','price') #without
    queryset = Product.objects.select_related('category').select_related('brand').all() #to get data from foreignkey relation speed
    return render(request,'products/list.html',{'data':queryset})




class Product_list(ListView):
    model = Product
    paginate_by = 100

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
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all().annotate(category_count = Count('product_category'))
        return context
    

class Brand_list(ListView):
    model = Brand
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brands"] = Brand.objects.all().annotate(brand_count=Count('product_brand'))
        return context
    

class Brand_detail(DetailView):
    model = Brand

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        myproducts = self.get_object()
        context["brand_products"] = Product.objects.filter(brand=myproducts)
        return context
    