from selenium import webdriver
import allure
import pytest


@allure.title("Verify the title of the webpage www.app.vwo.com")
def test_open_vwo_login():
    driver= webdriver.Chrome()  # post request to create copy of chrome and session id
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    page_source_data=driver.page_source
    assert "CURA Healthcare Service" in page_source_data
    driver.quit()