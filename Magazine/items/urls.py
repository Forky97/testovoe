from django.urls import path
from .views import *


urlpatterns = [


    path('api/get',ReadItemsApi.as_view(),name='get'),
    path('api/add',AddItemsApi.as_view(),name='add')

]
