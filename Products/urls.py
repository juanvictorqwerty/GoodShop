from django.urls import path
from .views import index
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path ("",index, name="index"),
    path ('admin/', admin.site.urls),
]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)