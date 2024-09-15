from django.contrib import admin
from .models import Product

## one way to register the class //admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description','price')

# Register your models here.
