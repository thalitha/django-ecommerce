from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>', views.product, name='product'),
    path('search', views.search, name='search'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]

