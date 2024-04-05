import json

import allure
import pytest
import requests


class TestCreatOrder:
    @pytest.mark.parametrize('color', ['BLACK', 'GREY', ''])
    @allure.title('Проверка создания заказа')
    def test_login_courier(self, color):
        payload = {
            "firstName": "firstName",
            "lastName": "lastName",
            "address": "address, 666 apt.",
            "metroStation": 32,
            "phone": "+7 800 111 11 11",
            "rentTime": 5,
            "deliveryDate": "2024-04-01",
            "comment": "Excuse me, sir",
            "color": color
        }
        payload_string = json.dumps(payload)
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders',
                                 data=payload_string)
        assert response.status_code == 201 and 'track' in response.json()
