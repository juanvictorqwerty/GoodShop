from django.shortcuts import render, HttpResponse

from Products.models import Product

def index (request,*args,**kwargs):
    list_products = Product.objects.all()
    context = { 
        'list_products':list_products  #dictionnary containing the products in the database
    }
    return render(request,"index.html",context)

















































# Create your views here.
