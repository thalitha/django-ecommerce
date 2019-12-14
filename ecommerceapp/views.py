from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.order_by('-created_date').filter(published=True)

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

def search(request):

    if 'search' in request.GET:
        filterSearch = request.GET['search']

    products = Product.objects.filter(name__icontains=filterSearch, published=True)

    data = {
        "products":products
    }
    return render(request,'search.html', data)