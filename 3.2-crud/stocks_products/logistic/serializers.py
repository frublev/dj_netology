from rest_framework import serializers
from .models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']
        # depth = 2


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    def create(self, validated_data):
        print(validated_data)
        positions = validated_data.pop('positions')
        print(positions)

        stock = super().create(validated_data)

        for p in positions:
            StockProduct.objects.update_or_create(
                stock=stock, product=p['product'], quantity=p['quantity'], price=p['price']
            )

        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')

        stock = super().update(instance, validated_data)

        for p in positions:
            StockProduct.objects.update_or_create(
                stock=stock, product=p['product'], quantity=p['quantity'], price=p['price']
            )

        return stock
