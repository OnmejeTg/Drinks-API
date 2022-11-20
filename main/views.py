from django.shortcuts import render
from .models import Drink
from .serializers import DrinkSerialiser
from django.http import JsonResponse
from rest_framework.response import Response

# Create your views here.
def drink_list(request):
    drinks = Drink.objects.all()
    serializer = DrinkSerialiser(drinks, many=True)

    return JsonResponse(serializer.data, safe=False)
