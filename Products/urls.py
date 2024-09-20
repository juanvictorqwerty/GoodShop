from django.urls import path
from .views import CreateProduct, index
from django.conf import settings
from django.conf.urls.static import static

app_name = "Products"

urlpatterns = [
    path ("",index, name="index"),
    #product creation form without using the admin
    path ("create-product/",CreateProduct.as_view(),name="create_product"), #create-product is an arbitrary name
]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)