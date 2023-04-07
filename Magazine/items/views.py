from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import  *
from .serializers  import *
from django.shortcuts import render
from rest_framework import permissions

from django.http import JsonResponse





class ReadItemsApi(APIView):

    def get(self, request):

        items = Product.objects.all()

        serializer = ProductSerializer(items,many=True)

        return Response(serializer.data)




class AddItemsApi(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        # Получаем данные из формы
        name = request.data.get('name')
        price = request.data.get('price')
        attributes = request.data.get('attributes')
        user = request.user

        print(request.data)

        if not name or not attributes:
            print('not name and str')


        print(f"Имя товара : {name}\nЦена товара : {price}\nХарактеристики товара: {attributes}")
        print(f"User: {user}")
        print(f"Атрибуты : {attributes}")

        product = Product(name=name, price=price, user=user)
        product.save()

        for attribute in attributes:
            characteristic_key = attribute.get('key')
            characteristic_value = attribute.get('value')

            characteristic = Characteristic(product=product, characteristic_key=characteristic_key,
                                            characteristic_value=characteristic_value)
            characteristic.save()


            print('ok')
            product_serializer = ProductSerializer(product)
            return Response(product_serializer.data)

        else:
            print('nok')
            return Response('nok')

def add_product(request):
    return render(request, 'form.html')




