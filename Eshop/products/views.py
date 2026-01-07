from django.shortcuts import render

from .models import Product

# Create your views here.
def productsView(request):
    template = 'products/products.html'
    context ={
        'products' : 'Product'
    }

    return render(request,template_name=template,context=context)
