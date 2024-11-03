import pytest

@pytest.fixture()
def create_token():
    return "abc"

@pytest.fixture()
def create_booking_id():
    return 1

@pytest.fixture()
def read_json_file():
    return "{}"
def test_consume( create_token,create_booking_id,read_json_file):
    print(create_booking_id)
    print(create_token)
    print(read_json_file)

def test_update_requirement1(create_token,create_booking_id):
    print("token=", create_token)
    print("bookingid=", create_booking_id)

def test_update_requirement2(create_token,create_booking_id):
    print("token=", create_token)
    print("bookingid=", create_booking_id)



