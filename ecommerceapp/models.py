from django.db import models
from datetime import datetime


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    category = models.CharField(max_length=200)
    image = models.ImageField(upload_to="img", blank=True, null=True)

class Order(models.Model):
    user_id = models.IntegerField()
    created_date = models.DateTimeField(default=datetime.now, blank=True)

class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)