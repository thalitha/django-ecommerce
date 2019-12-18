from django.urls import path

from . import views

urlpatterns = [
    path('<int:order_product_id>', views.HomePageView.as_view(), name='payments'),
    path('charge/<int:product_id>/<int:user_id>/', views.charge, name='charge'),
]