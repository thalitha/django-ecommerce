from django.shortcuts import render



# Create your views here.
def index(request):
    products ={
        1:"Awesome Brown",
        2:"Light Pink and White",
        3:"Black and Pink"
    }

    dados = {
        "product_names":products
    }
    return render(request,'index.html', dados)

def product(request):
    return render(request,'product.html')