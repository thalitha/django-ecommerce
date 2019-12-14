from django.db import models
from ecommerceapp.models import Product
from datetime import datetime

# Create your models here.
class Order(models.Model):
    user_id = models.IntegerField()
    created_date = models.DateTimeField(default=datetime.now, blank=True)

class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
