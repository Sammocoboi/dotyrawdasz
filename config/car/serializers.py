from rest_framework import serializers
from .models import Car,Firm

class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm 
        fields = ['name']

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car 
        fields = ['name','firm']