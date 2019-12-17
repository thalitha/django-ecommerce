from django.urls import path

from . import views

urlpatterns = [
    path('<int:order_product_id>', views.HomePageView.as_view(), name='payments'),
    path('charge/', views.charge, name='charge'),
]