import stripe
from django.conf import settings
from django.views.generic.base import TemplateView
from django.shortcuts import render, get_list_or_404, get_object_or_404
from ecommerceapp.models import Product
from sales.models import Order, Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        product = get_object_or_404(Product, pk=kwargs['order_product_id'])
      
        context['name'] = product.name
        context['price'] = product.price
        context['product_id'] = kwargs['order_product_id']
        return context


def charge(request, product_id, user_id): # new
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description='Old Currnecy',
            source=request.POST['stripeToken']
        )

        product = get_object_or_404(Product, pk=product_id)

        order = Order()
        order.user_id = user_id
        order.save()

        item = Item()
        item.order = order
        item.quantity = 1
        item.product = product
        item.total = product.price
        item.save() 

        data = {
                "product_id":product_id,
                "user_id":user_id,
                "price":product.price,
                "orderid":order.id
        }
      
        return render(request, 'charge.html', data)