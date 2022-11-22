from rest_framework import serializers

from bank.models import Category, Currency, Transactions

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('id', 'code', 'name')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')

class ReadTransactionSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer()

    class Meta:
        model = Transactions
        fields =  ('id', 'amount', 'currency', 'date', 'description', 'category')
        read_only_fields = fields

class WriteTransactionSerializer(serializers.ModelSerializer):
    currency = serializers.SlugRelatedField(slug_field="code", queryset=Currency.objects.all())

    class Meta:
        model = Transactions
        fields =  ( 'amount', 'currency', 'date', 'description', 'category')