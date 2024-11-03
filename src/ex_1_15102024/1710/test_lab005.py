import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import allure
import pytest


@allure.title("Verify the title of the webpage www.app.vwo.com")
def test_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--window-size=900,600")
    chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-infobars")
    driver= webdriver.Chrome(chrome_options)  # post request to create copy of chrome and session id
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    # page_source_data=driver.page_source

    assert True == False
    #time.sleep(10)