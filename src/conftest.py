import allure
import pytest
import requests
from dotenv import load_dotenv

import fixtures
import os


@allure.title("Test Authentication")
@allure.description("tc2-verify that get request with id works")
@pytest.mark.crud
@pytest.fixture()
def create_token():
    load_dotenv()
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    url = "https://restful-booker.herokuapp.co/auth"
    headers={"Content-Type":"application/json"}
    json_payload = {
        "username" : username,
        "password" : password
    }
    response = requests.post(url=url,headers=headers,json=payload)
    assert response.status_code == 200

    token = response.json()["token"]
    print(token)
    return token

@pytest.fixture()
def create_booking():
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code == 200
    print(type(URL))
    print(type(headers))
    print(type(json_payload))

    Data = response.json()

    bookingid = Data["bookingid"]
    return bookingid
@pytest.fixture()
def test_put_request(create_token,create_booking_id):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking_id())
    put_URL = base_url + base_path
    cookie ="cookie=" + create_token()
    headers ={
        "Content-Type": "application/json",
        "Cookie": cookie
    }

    json_payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=put_URL, headers=headers, json=json_payload)
    data = response.json()
    print(data)
    assert response.status_code == 200
    assert data["firstname"] == "Jim"

@pytest.fixture()
def test_delete_request():
    URL = "https://restful-booker.herokuapp.com/booking"
    booking_id = create_booking()
    DELETE_URL = URL + str(booking_id)
    cookie_value = "token=" + create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie_value
    }
    print(headers)
    response = requests.delete(url=DELETE_URL, headers=headers)


