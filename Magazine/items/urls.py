from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [


    path('api/get',ReadItemsApi.as_view(),name='get'),
    path('api/add',AddItemsApi.as_view(),name='add'),
    path('api/test',add_product,name='test'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
