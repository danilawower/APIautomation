import random

import requests

url = 'https://demoqa.com/'


def test_get_bookstore():
    response = requests.get(url + '/BookStore/BookStoreV1BooksGet/')
    assert response.status_code == 200


def test_authorized():
    creds = credentials()
    login = authorize(creds)
    assert login.status_code == 200


def test_generate_token():
    creds = credentials()
    generate_token = requests.post(url + 'Account/V1/GenerateToken/', json=creds)
    token = generate_token.json()
    token_data = token['token']
    assert type(token_data) == str


def test_registration():
    new_creds = {
            "userName": f"TestUser{random.randint(1, 99)}",
            "password": f"Password@_{random.randint(1, 99)}"
        }
    registration = requests.post(url + 'Account/v1/User', json=new_creds)
    assert registration.status_code == 201


def test_get_uuid():
    uuid_data = generate_uuid()
    get_user = requests.get(url + 'Account/v1/User' + uuid_data)
    assert get_user.status_code == 200










def login():
    creds = credentials()
    authorize(creds)


def authorize(creds):
    return requests.post(url + 'Account/v1/Authorized', json=creds)


def credentials():
    return {
        "userName": "username1",
        "password": "@#wTmBpo4"
    }

def generate_token():
    creds = credentials()
    generate_token = requests.post(url + 'Account/V1/GenerateToken/', json=creds)
    token = generate_token.json()
    token_data = token['token']
    return token_data


def generate_uuid():
    new_creds = {
            "userName": f"TestUser{random.randint(1, 99)}",
            "password": f"Password@_{random.randint(1, 99)}"
        }
    registration = requests.post(url + 'Account/v1/User', json=new_creds)
    response = registration.json()
    uuid = response['userID']
    return uuid



