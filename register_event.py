# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.keys import Keys
#
#
# # URL of the webpage ASANA
# URL_Homepage ="https://asana.com/"
# URl_RegisterPage ="https://asana.com/work-innovation-summit-watch-party#form"
#
# driver = webdriver.Chrome()
# driver.get(URl_RegisterPage)
#
# driver.implicitly_wait(100000000)
#
#
# # Registering Details of the Test User Eg: FirstName John and LastName : Doe
# first_name = driver.find_element(By.ID, 'FirstName')
# first_name.send_keys("John")
#
# last_name = driver.find_element(By.ID, 'LastName')
# last_name.send_keys("Doe")
#
# email1= driver.find_element(By.ID,'Email')
# email1.send_keys("johnDoetest1@gmail.com")
#
# Company1= driver.find_element(By.ID,'Company')
# Company1.send_keys('TestCompany1')
#
# drop=Select(driver.find_element(By.ID,'Country'))
# drop.select_by_visible_text("India")
#
# Job_title= driver.find_element(By.ID,'Title')
# Job_title.send_keys('SelenimumSE5235Tester')
#
# drop1=Select(driver.find_element(By.ID,'NumberOfEmployees'))
# drop1.select_by_index(1)
#
#
# time.sleep(4)
#
# submit= driver.find_element(By.CLASS_NAME,"mktoButton")
# submit.click()
# time.sleep(5)
# # element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'mktoButton®')))
#
#
# #the Event which required resgistration is over , hence the test case as been changed.
# # text_retrived = driver.find_element(By.CLASS_NAME, 'content')
# #
# # if "Thank You" in text_retrived.text:
# #     print("PASS")
#
# time.sleep(10)
#
# driver.implicitly_wait(10)
# driver.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

URL_Homepage = "https://asana.com/"
URl_RegisterPage = "https://asana.com/work-innovation-summit-watch-party#form"


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_registration(driver):
    driver.get(URl_RegisterPage)

    first_name = driver.find_element(By.ID, 'FirstName')
    first_name.send_keys("John")

    last_name = driver.find_element(By.ID, 'LastName')
    last_name.send_keys("Doe")

    email1 = driver.find_element(By.ID, 'Email')
    email1.send_keys("johnDoetest1@gmail.com")

    Company1 = driver.find_element(By.ID, 'Company')
    Company1.send_keys('TestCompany1')

    drop = Select(driver.find_element(By.ID, 'Country'))
    drop.select_by_visible_text("India")

    Job_title = driver.find_element(By.ID, 'Title')
    Job_title.send_keys('SeleniumSE5235Tester')

    drop1 = Select(driver.find_element(By.ID, 'NumberOfEmployees'))
    drop1.select_by_index(1)

    time.sleep(4)

    submit = driver.find_element(By.CLASS_NAME, "mktoButton")
    submit.click()
    time.sleep(5)

    # Add any assertions you want to perform after submitting the form
    # Example:
    # assert "Thank You" in driver.page_source

    time.sleep(10)

if __name__ == "__main__":
    pytest.main([__file__])