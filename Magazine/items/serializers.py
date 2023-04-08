from rest_framework import serializers
from .models import *

class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = ('characteristic_key', 'characteristic_value')


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = ('image')




class ProductSerializer(serializers.ModelSerializer):
    characteristics = CharacteristicSerializer(many=True)  # Сериализатор для характеристик
    images = serializers.StringRelatedField(many=True, read_only=True)


    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'created_at', 'user', 'characteristics','images')


