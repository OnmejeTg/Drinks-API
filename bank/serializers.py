from rest_framework import serializers

from bank.models import Category, Currency

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('id', 'code', 'name')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        name = Category
        fields = ('id','name')