from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet

from bank.models import Category, Currency
from bank.serializers import CategorySerializer, CurrencySerializer


class CurrencyListAPIView(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

# @api_view(['GET'])
# def currencies(request):
#     currencies = Currency.objects.all()
#     serializer = CurrencySerializer(currencies, many=True)

#     return Response(serializer.data)

class CategoryModelViewSet(ModelViewSet):
    queryset =Category.objects.all()
    serializer_class = CategorySerializer