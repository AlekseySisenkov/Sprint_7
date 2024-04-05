import pytest

from helper import generate_login_password, register_new_courier_and_return_login_password


@pytest.fixture(scope='function')
def generate_login():
    return generate_login_password()['login']


@pytest.fixture(scope='function')
def generate_password():
    return generate_login_password()['password']


@pytest.fixture(scope='function')
def generate_firstName():
    return generate_login_password()['firstName']


@pytest.fixture(scope='function')
def current_login_password(generate_login, generate_password):
    return register_new_courier_and_return_login_password(generate_login, generate_password)
