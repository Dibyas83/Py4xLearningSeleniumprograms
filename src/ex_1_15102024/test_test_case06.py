import allure
import pytest
import requests


@allure.title("Test Authentication")
@allure.description("tc2-verify that get request with id works")
@pytest.mark.crud
def test_create_booking_negative_tc6():
    base_url = "https://restful-booker.herokuapp.com"
    base_path="/booking"
    URL = base_url + base_path
    headers={"Content-Type":"application/json"}
    json_payload = {}

    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))

    assert response.status_code == 500