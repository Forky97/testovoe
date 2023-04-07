from rest_framework import serializers
from .models import *

class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = ('characteristic_key', 'characteristic_value')



class ProductSerializer(serializers.ModelSerializer):
    characteristics = CharacteristicSerializer(many=True)  # Сериализатор для характеристик

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'created_at', 'user', 'characteristics')

    def create(self, validated_data):
        characteristics_data = validated_data.pop('characteristics')
        product = Product.objects.create(**validated_data)
        for char_data in characteristics_data:
            Characteristic.objects.create(product=product, **char_data)
        return product

    def update(self, instance, validated_data):
        characteristics_data = validated_data.pop('characteristics')
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.user = validated_data.get('user', instance.user)
        instance.characteristics.all().delete()  # Удаляем все существующие характеристики
        for char_data in characteristics_data:
            Characteristic.objects.create(product=instance, **char_data)
        instance.save()
        return instance