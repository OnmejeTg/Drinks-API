from rest_framework import serializers
from .models import Drink

class DrinkSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = '__all__'