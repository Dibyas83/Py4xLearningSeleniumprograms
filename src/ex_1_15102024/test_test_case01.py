import pytest
import allure


@allure.title("sum")
@allure.description("This test attempts to log into the website using a login and a password.")
@pytest.mark.regr()
def test_verify_summ():
    assert 1+1 == 2

@allure.title("multiplication")
@allure.description("This test attempts to log into the website using a login and a password.")
@pytest.mark.regr()
def test_verify_multi():
    assert 2*1 == 2

@allure.title("sum2")
@allure.description("This test attempts to log into the website using a login and a password.")
@pytest.mark.regr()
def test_verify_sum2():
    assert 2+1 == 3

@allure.title("sum11")
@allure.description("This test attempts to log into the website using a login and a password.")
@pytest.mark.mock()
def test_verify_subs():
    assert 2-1 == 1

@allure.title("sum10")
@allure.description("This test attempts to log into the website using a login and a password.")
@pytest.mark.skip("reason incomplete")
def tes_verify_multi():
    assert 5*2 == 10
@allure.title("sum5")
@allure.description("This test attempts to log into the website using a login and a password.")
@pytest.mark.mock()
def test_test_ok():
    assert 1+4 == 5