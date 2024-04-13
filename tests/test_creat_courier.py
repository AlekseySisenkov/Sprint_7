import allure
import requests

from data import url, courier


class TestCreatCourier:
    @allure.title('Проверка создания курьера')
    def test_creat_courier(self, generate_login, generate_password, generate_firstName):
        payload = {
            "login": generate_login,
            "password": generate_password,
            "firstName": generate_firstName
        }
        response = requests.post(url+courier, data=payload)
        assert response.status_code == 201 and response.json()['ok'] == True

    @allure.title('Проверка дубля курьера')
    def test_double_courier(self, generate_login, generate_password, generate_firstName):
        payload = {
            "login": generate_login,
            "password": generate_password,
            "firstName": generate_firstName
        }
        response1 = requests.post(url+courier, data=payload)
        response2 = requests.post(url+courier, data=payload)
        assert response2.status_code == 409 and response2.json()["message"] == ("Этот логин уже используется. "
                                                                                "Попробуйте другой.")

    @allure.title('Проверка обязательности поля login')
    def test_creat_courier_without_login(self, generate_password, generate_firstName):
        payload = {
            "password": generate_password,
            "firstName": generate_firstName
        }
        response = requests.post(url+courier, data=payload)
        assert response.status_code == 400 and response.json()["message"] == ('Недостаточно данных для '
                                                                              'создания учетной записи')

    @allure.title('Проверка обязательности поля password')
    def test_creat_courier_without_password(self, generate_login, generate_firstName):
        payload = {
            "login": generate_login,
            "firstName": generate_firstName
        }
        response = requests.post(url+courier, data=payload)
        assert response.status_code == 400 and response.json()["message"] == ('Недостаточно данных для создания '
                                                                              'учетной записи')
