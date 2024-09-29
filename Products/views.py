from django.shortcuts import render, HttpResponse
from Products.models import Product
from django.views import View

def index(request) :
    return render(request,"index.html")

def shop (request,*args,**kwargs):
    list_products = Product.objects.all()
    context = { 
        'list_products':list_products  #dictionnary containing the products in the database
    }
    return render(request,"shop.html",context)



















































# Create your views here.
