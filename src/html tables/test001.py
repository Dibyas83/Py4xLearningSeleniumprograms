from lib2to3.pgen2 import driver

from  selenium import webdriver
from selenium.webdriver.common.by import By


def test_webtables():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")
    driver.maximize_window()

#col
# //table[contains(@ id, "cust")] / tbody / tr
row_elements = driver.find_elements(By.XPATH,"//table[contains(@ id, "cust")] / tbody / tr")
row = len(row_elements)
print(row)

#col
# // table[contains(@ id, "cust")] / tbody / tr(2)/td
col_elements = driver.find_elements(By.XPATH,"//table[contains(@ id, "cust")] / tbody / tr(2)/td")
col=len(col_elements)
print(col)
first_part="//table[contains(@ id, "cust")] / tbody / tr["
sec_part = "]/td["
third_part ="]"
for i in range(2,row+1):
    for j in range(1,col+1):
        dynamic_path = f "(first_part){i}(sec_part){j}(third_part)"
        #print(dynamic_path)
        data = driver.find_element(By.XPATH.dynamic_path)
        #print(driver.find_element(dynamic_path).text.end=" ")
        print(data.text,end="")
        if "Helen Bennett" in data:
            country_path = f"(dynamic_path)/following-sibling::td"
            country_text = driver.find_element(By.XPATH,country_path).text
            print(f"Helen Bennet is in {country_text}")

        driver.get("https://awesomeqa.com/webtable1.html")
        table = table.find_element(By.XPATH,"//table[@summary="Sample Table"]/tbody")
        # row_table = "//table[@summary="Sample Table"]/tr")
        row_table= table.find_element(By.TAG_NAME,"tr")

        for row in row_table:
            col = row.find_elements(By.TAG_NAME,"td")
            for e in col:
                print(e.text)












