from django.urls import path

from . import views
from customers.views import register

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>', views.product, name='product'),
    path('search', views.search, name='search'),
    path('register', register, name='register'),
]

