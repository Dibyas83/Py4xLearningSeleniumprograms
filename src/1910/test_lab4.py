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


    # relative xpath copy as xpath
    # //*[@id="login-username"]
    # //*[@data-qa="hocewoqisi"
    # copy as full xpath
    # /html/body/div[2]/div[1]/div[2]/div/div[1]/div/div/div[3]/form[1]/ul/li[1]/div/input
    first_name_input_tag = driver.find_element(By.XPATH,"//input[@placeholder='First Name']")
    first_name_input_tag.send_keys("Hello")

    # //a[contains(text(),"Make Appointment") and contains(id="btn-make-appointment")]
    # //a[starts-with(text(),"Make")]
    # //a[normalize-space()="Make")]
    # //div[@class="Mammal"]/following-sibling::div
    # //div[@class="Mammal"]/preceding-sibling::div
    # //div[@class="Mammal"]/ancestor::div



    time.sleep(5)
    driver.quit()