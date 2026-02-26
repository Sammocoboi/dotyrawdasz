
import pytest
from car.models import Firm, Car


@pytest.mark.django_db
def test_firm_creation(firm):
  
    assert firm.name == "Toyota"
    assert firm.id is not None
@pytest.mark.django_db
def test_firm_str_method(firm):

    assert str(firm) == "Toyota"


@pytest.mark.django_db
def test_car_creation(car, firm):

    assert car.name == "Camry"
    assert car.model == "XV70"
    assert car.firm == firm
@pytest.mark.django_db
def test_car_str_method(car):

    assert str(car) == "Camry"
@pytest.mark.django_db
def test_car_foreign_key_relation(car, firm):

    assert firm.car_set.count() == 1
    assert firm.car_set.first() == car
@pytest.mark.django_db
def test_cascade_delete(firm):

    Car.objects.create(name="Corolla", model="E210", firm=firm)

    assert Car.objects.filter(firm=firm).count() == 1
    

    firm_id = firm.id
    firm.delete()
   
    assert not Firm.objects.filter(id=firm_id).exists()

    assert Car.objects.filter(firm_id=firm_id).count() == 0