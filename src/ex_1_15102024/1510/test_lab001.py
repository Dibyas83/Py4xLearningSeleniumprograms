from selenium import webdriver
import allure
import pytest


@allure.title("Verify the title of the webpage www.google.com")
def test_sample():
    driver= webdriver.Edge()  # post request to create copy of chrome and session id
    driver.get("https://www.google.com")
    driver.title
    assert driver.current_url == "https://www.google.com/"
