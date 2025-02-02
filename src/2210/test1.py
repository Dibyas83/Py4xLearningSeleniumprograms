import time

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By


@allure.title("Find all the buttons by TagName")
@allure.description("Verify that FREE Trail button is clicked, Navigated to next page")
def test_5():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")

    first_name_input_tag = driver.find_element(By.CSS_SELECTOR,"")
    first_name_input_tag.send_keys("Hello")
    # div.first span:nth-child(2n)
    # img[title="Flipkart"] exact match
    # img[title*="Flip"]   cotains or partial
    # img[title*^="Flip"]   starts with
    # img[title$="art"]   ends with
    # div.s-item__title
    # //div[@class="s-item__title"]



    time.sleep(5)
    driver.quit()