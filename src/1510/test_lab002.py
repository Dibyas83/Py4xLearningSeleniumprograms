from selenium import webdriver
import allure
import pytest


@allure.title("Verify the title of the webpage www.app.vwo.com")
def test_open_vwo_login():
    driver= webdriver.Chrome()  # post request to create copy of chrome and session id
    driver.get("https://app.vwo.com")
    print(driver.title)  # get request
    assert driver.title == "Login - VWO"  # get request
    assert driver.current_url == "https://app.vwo.com/#/login"