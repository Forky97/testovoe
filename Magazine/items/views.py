from rest_framework import status
from .serializers  import *
from django.shortcuts import render
from django.dispatch import receiver
from django.db.models.signals import pre_delete
import json
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
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
        print(request.data)


        name = request.data.get('name')
        price = request.data.get('price')
        attributes = request.data.get('attributes')
        user = request.user
        images = request.FILES.getlist('images')


        if all([x is not None for x in [price, attributes, user]]) and len(name) != 0:
            product = Product(name=name, price=price, user=user)
            product.save()

            attributes = json.loads(attributes)  # Преобразуем строку JSON в словарь


            for attribute in attributes:
                characteristic_key = attribute.get('key')
                characteristic_value = attribute.get('value')

                characteristic = Characteristic(product=product, characteristic_key=characteristic_key,
                                                characteristic_value=characteristic_value)
                characteristic.save()

                print('ok')

            for image in images:
                product_image = ProductImage(image=image)
                product_image.save()
                product.images.add(product_image)

            product_serializer = ProductSerializer(product)
            return Response(product_serializer.data)

        else:
            return Response('error', status=status.HTTP_400_BAD_REQUEST)




def add_product(request):
    return render(request, 'form.html')

@receiver(pre_delete, sender=Product)
def delete_product_images(sender, instance, **kwargs):
    # Удаляем все изображения, связанные с продуктом
    instance.images.all().delete()




