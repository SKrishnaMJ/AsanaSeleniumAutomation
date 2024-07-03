# This code has two test cases integrated,
# (i) is to check if we can access the inbox
# (ii) is to check if send message button works

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login_and_send_message(browser):
    browser.get("https://app.asana.com/-/login?_gl=1*1rzaf95*_ga*OTM2MDAxNDgzLjE2OTc4NjIzNjM.*_ga_J1KDXMCQTH*MTY5ODAzOTY2NC4yLjEuMTY5ODA0MDM5NC4wLjAuMA..*_fplc*UThZUlB4NU9NJTJCaENDQml6dG5mUTRHRHZpQ2UyaWNGMllrTlh2aG9udVRWUWFRclJVY2hMJTJGcnR0WW5Qdk9jUURMckd3QzNuUGRVWUQyS09zdmlpWXpkYVdKejBKUm10RndpSWRMNDRaWDdLOFFFZzcxazQxdnNlVVdRR1BPZyUzRCUzRA..")

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
    time.sleep(7)

    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[1])
    browser.get('https://app.asana.com/0/inbox/1205772387108322')

    btn_wait = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[2]/div/main/div[2]/div/div[1]/div[2]/div[1]/div')))

    send_msg_btn = browser.find_element(By.CLASS_NAME, 'PencilPadMiniIcon')
    send_msg_btn.click()
    time.sleep(8)
    heading_text = browser.find_element(By.CLASS_NAME, 'PopOutStructure-header')
    print(heading_text.text)
    time.sleep(2)

if __name__ == "__main__":
    pytest.main([__file__])