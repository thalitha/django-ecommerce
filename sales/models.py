from django.db import models
from ecommerceapp.models import Product
from customers.models import Customer
from datetime import datetime

# Create your models here.
class Order(models.Model):
    user_id = models.IntegerField()
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    def __int__(self):
        return self.id

class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
