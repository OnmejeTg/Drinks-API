from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from bank.models import Category, Currency, Transactions
from bank.serializers import CategorySerializer, CurrencySerializer, ReadTransactionSerializer, WriteTransactionSerializer


class CurrencyListAPIView(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = None

# @api_view(['GET'])
# def currencies(request):
#     currencies = Currency.objects.all()
#     serializer = CurrencySerializer(currencies, many=True)

#     return Response(serializer.data)

class CategoryModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset =Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None

class TransactionModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend,)
    search_fields = ('description',)
    ordering_fields = ('amount', 'date',)
    filterset_fields = ('currency__code',)
    

    def get_queryset(self):
        return Transactions.objects.select_related("currency", "category", "user").filter(user=self.request.user)


    def get_serializer_class(self):
        if self.action in ("list", "retrive"):
            return ReadTransactionSerializer
        return WriteTransactionSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
