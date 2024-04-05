import json

import allure
import requests


class TestListOfOrders:
    @allure.title('Получение списка заказов')
    def test_login_courier_without_login(self):
        payload = {
            "courierId": 1,
            "nearestStation": ["1", "2"],
            "limit": 12,
            "page": 12
        }
        payload_string = json.dumps(payload)
        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders',
                                data=payload_string)
        assert response.status_code == 200 and 'orders' in response.json()
