from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Product
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import logout, authenticate, login

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


# def register(request):
#     form = UserCreationForm
#     return render(request, template_name = "register.html", context={"form":form})

def register(request):
    form = UserCreationForm
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # username = form.cleaned_data.get('username')
            # login(request, user)
            return redirect("index")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
            return render(request, template_name = "register.html",  context={"form":form})

    return render(request, template_name = "register.html", context={"form":form})
