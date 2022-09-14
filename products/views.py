from django.shortcuts import render
from .models import Product , ProductImage , Review
from django.views.generic import ListView , DetailView
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
    
    
    