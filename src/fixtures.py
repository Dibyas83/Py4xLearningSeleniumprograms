import pytest

@pytest.fixture()
def is_married():
    return True

def test_confirm(is_married):
    assert is_married == False
