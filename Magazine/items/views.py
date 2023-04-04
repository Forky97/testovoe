from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import  *
from .serializers  import *



class ReadItemsApi(APIView):

    def get(self, request):
        items = Item.objects.all()

        serializer = ProductSerializer(items, many=True)

        return Response(serializer.data)




class AddItemsApi(APIView):

    def post(self, request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            product = serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







