from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()

    data = {
        "products":products
    }
    return render(request,'index.html', data)

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product_return = {
        'product': product
    }
    return render(request,'product.html',product_return)