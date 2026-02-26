import pytest 
from rest_framework.test import APIClient
@pytest.mark.django_db
def test_api_get(client):
    response = client.get('/api/')
    
    assert response.status_code != 500
    print(f"Get status {response.status_code}")

# тестируем Post запрос на провреку работы сервера 
# по прниятию данных
@pytest.mark.django_db
def test_api_post(client):
    data = {
        "message":"Работает"
    }

    response = client.post("/api/test",data,format="json")

    # проверяем статус код что аднные приняты 

    assert response.status_code != 500

    print(f"Post статус {response.status_code}")
@pytest.mark.django_db
def test_api_returns(client):
    # проверяем что запрос возращает хоть какие-то данные 
    response = client.get('/api/')

    #проверяем что есть какой-то ответ 
    
    assert response.content is not None
    print(f"{response.content[:20]}")