import pytest
import allure

@allure.title("Test Authentication")
@allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")

@pytest.mark.regr()
def test_verify_summ():
    assert 1+1 == 2


@pytest.mark.mock()
def test_verify_subs():
    assert 2-1 == 1


@pytest.mark.skip("reason incomplete")
def tes_verify_multi():
    assert 5*2 == 10

@pytest.mark.mock()
def test_test_ok():
    assert 1+4 == 5