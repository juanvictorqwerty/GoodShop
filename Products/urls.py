from django.urls import path
from .views import  index, shop
from django.conf import settings
from django.conf.urls.static import static

app_name = "Products"

urlpatterns = [
    path ("",index, name="index"),
    path("shop/",shop, name="shop")
    #product creation form without using the admin
    
]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)