from django.shortcuts import render, HttpResponse
from Products.models import Product
from django.views import View

def index (request,*args,**kwargs):
    list_products = Product.objects.all()
    context = { 
        'list_products':list_products  #dictionnary containing the products in the database
    }
    return render(request,"index.html",context)


class CreateProduct(View) :

    def get(self, request, *args,**kwargs):
        return render(request,"Products_created/create_product.html")
        
    
    def post(self,request,*args,**kwargs):
        
        name = request.POST.get('name')
        description= request.POST.get('description')
        price= request.POST.get('price')
        image= request.FILES.get('image')

        product = Product.objects.create(name =name, description=description,price=price,image=image)
        
        if product:
            return HttpResponse("Successfully saved")
        else:
            return HttpResponse("Error")
















































# Create your views here.
