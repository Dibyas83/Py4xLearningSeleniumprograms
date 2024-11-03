import allure
import pytest
import requests


@allure.title("Test Authentication")
@allure.description("tc2-verify that get request with id works")
@pytest.mark.crud
def test_create_booking_bug_tc5(): # totalprice
    base_url = "https://restful-booker.herokuapp.com"
    base_path="/booking"
    URL = base_url + base_path
    headers={"Content-Type":"application/json"}
    payload={
        "firstname" : "Jim",
        "lastname" : "Brown",
        "totalprice" : "pramod",
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2018-01-01",
            "checkout" : "2019-01-01"
        },
        "additionalneeds" : "Breakfast"
    }
    response = requests.post(url=URL,headers=headers,json=payload)
    assert response.status_code == 200

    responseData = response.json()

    bookingid = responseData["bookingid"]
    assert bookingid is not None
    assert bookingid > 0
    assert type(bookingid) == int

    firstname = responseData["booking"]["firstname"]
    lastname = responseData["booking"]["lastname"]
    totalprice = responseData["booking"]["totalprice"]
    depositpaid = responseData["booking"]["depositpaid"]

    assert firstname == "Jim"
    assert lastname == "Brown"
    assert totalprice == None
    assert depositpaid == True