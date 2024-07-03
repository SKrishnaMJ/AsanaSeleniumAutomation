import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login_to_asana(browser):
    browser.get(
        'https://app.asana.com/-/login?_gl=1*1rzaf95*_ga*OTM2MDAxNDgzLjE2OTc4NjIzNjM.*_ga_J1KDXMCQTH*MTY5ODAzOTY2NC4yLjEuMTY5ODA0MDM5NC4wLjAuMA..*_fplc*UThZUlB4NU9NJTJCaENDQml6dG5mUTRHRHZpQ2UyaWNGMllrTlh2aG9udVRWUWFRclJVY2hMJTJGcnR0WW5Qdk9jUURMckd3QzNuUGRVWUQyS09zdmlpWXpkYVdKejBKUm10RndpSWRMNDRaWDdLOFFFZzcxazQxdnNlVVdRR1BPZyUzRCUzRA..')
    ele_wait = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.NAME, 'e')))
    login = browser.find_element(By.NAME, 'e')
    login.send_keys('sxm9759@mavs.uta.edu')
    time.sleep(3)
    submit = browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/form/div[2]')
    submit.click()
    time.sleep(3)
    password = browser.find_element(By.NAME, 'p')
    password.send_keys('Edenhazard1!')
    time.sleep(3)
    submit_pass = browser.find_element(By.CLASS_NAME, 'LoginPasswordForm-loginButton')
    submit_pass.click()
    time.sleep(6)

def test_add_task(browser):
    test_login_to_asana(browser)
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[1])
    browser.get('https://app.asana.com/0/1205772387108327/list')
    btn_wait = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'AddTaskDropdownButton')))
    add_task = browser.find_element(By.CLASS_NAME, 'AddTaskDropdownButton')
    add_task.click()
    time.sleep(7)
    task = browser.find_element(By.CLASS_NAME, 'SpreadsheetTaskName')
    task.send_keys('New Task by Sai Krishna')
    task.send_keys(Keys.ENTER)
    time.sleep(8)

    # Close the second window after the test
    browser.close()
    browser.switch_to.window(browser.window_handles[0])

if __name__ == "__main__":
    pytest.main([__file__])