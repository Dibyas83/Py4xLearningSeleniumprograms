import pytest
import allure
import requests

@allure.title("Test Authentication")
@allure.description("verify that get request with id works")
@allure.tag("Regression","po", "smoke", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.testcase("TC1")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url)
    print(response_data.text)
    print(response_data.json())
    print(response_data.headers)
    assert response_data.status_code == 200


@allure.title("Test Authentication")
@allure.description("tc2-verify that get request with id works")
@allure.testcase("TC2")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url)
    assert response_data.status_code == 200

