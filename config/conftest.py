import pytest 
from car.models import Car,Firm
from rest_framework.test import APIClient
import os
import django

@pytest.fixture
def firm():
    return Firm.objects.create(name="Toyota")

@pytest.fixture
def car(firm):
    return Car.objects.create(
        name="Camry", 
        model="XV70", 
        firm=firm
    )


@pytest.fixture
def client():
    # фиктсура для создания клиента api 
    return APIClient()