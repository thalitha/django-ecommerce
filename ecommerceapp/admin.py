from django.contrib import admin
from .models import Product

# Register your models here.
class ProductList(admin.ModelAdmin):
    list_display = ('id','name','category','price','published')
    list_display_links =  ('id','name','category','price')
    search_fields = ('name',)
    list_filter = ('category',)
    list_editable =('published',)
    list_per_page = 10

admin.site.register(Product, ProductList)
