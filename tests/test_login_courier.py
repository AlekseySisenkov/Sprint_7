import allure
import requests


class TestLoginCourier:
    @allure.title('Проверка успешного входа существующего курьера')
    def test_login_courier(self, current_login_password):
        payload = {
            "login": current_login_password[0],
            "password": current_login_password[1]
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
                                 data=payload)
        assert response.status_code == 200 and 'id' in response.json()

    @allure.title('Проверка входа курьера без логина')
    def test_login_courier_without_login(self, current_login_password):
        payload = {
            "login": '',
            "password": current_login_password[1]
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
                                 data=payload, timeout=10)
        assert response.status_code == 400 and response.json()["message"] == 'Недостаточно данных для входа'

    @allure.title('Проверка входа курьера без пароля')
    def test_login_courier_without_password(self, current_login_password):
        payload = {
            "login": current_login_password[0],
            "password": ''
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
                                 data=payload, timeout=10)
        assert response.status_code == 400 and response.json()["message"] == 'Недостаточно данных для входа'

    @allure.title('Проверка входа курьера несуществующей парой логин-пароль')
    def test_login_courier_with_incorrect_login_password(self):
        payload = {
            "login": "incorrect_login",
            "password": 'incorrect_password'
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
                                 data=payload, timeout=10)
        assert response.status_code == 404 and response.json()["message"] == 'Учетная запись не найдена'
