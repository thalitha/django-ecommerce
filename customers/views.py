from django.shortcuts import render
from .models import Customer
# Create your views here.
def register(request):
    return render(request,'register.html')