import time

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By


@allure.title("Print the Titles of the Ebay sites after searching")
@allure.description("Verify that 62 items are there for macmini")
def test_5(list_of_items=None):
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")

    search_box_input_xpath = driver.find_element(By.XPATH, "//input[@placeholder='Search for anything']")
    # search_box_inout_css = driver.find_element(By.CSS_SELECTOR,"#gh-ac")
    search_box_input_xpath.send_keys("macmini")

    search_box_button = driver.find_element(By.CSS_SELECTOR, "input[value='Search']")
    search_box_button.click()

    list_of_items = driver.find_elements(By.CSS_SELECTOR, ".s-item__title")
    list_of_items_prize = driver.find_elements(By.CSS_SELECTOR, ".s-item__price")
    len_items = len(list_of_items)
    len_of_items_price = len(list_of_items_prize)
    min_items = min(len_items,len_of_items_price)
    print(min_items)

    print(list_of_items[0].text)

    #for i in range(1,min_items+1):
     #   print(i)

       # print(list_of_items[i].text + "_" + list_of_items_prize[i].text)


    assert len(list_of_items) == 62



    time.sleep(5)
    driver.quit()