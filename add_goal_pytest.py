import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_asana_workflow(browser):
    # Initial Initialization
    browser.get("https://app.asana.com/-/login?_gl=1*1rzaf95*_ga*OTM2MDAxNDgzLjE2OTc4NjIzNjM.*_ga_J1KDXMCQTH*MTY5ODAzOTY2NC4yLjEuMTY5ODA0MDM5NC4wLjAuMA..*_fplc*UThZUlB4NU9NJTJCaENDQml6dG5mUTRHRHZpQ2UyaWNGMllrTlh2aG9udVRWUWFRclJVY2hMJTJGcnR0WW5Qdk9jUURMckd3QzNuUGRVWUQyS09zdmlpWXpkYVdKejBKUm10RndpSWRMNDRaWDdLOFFFZzcxazQxdnNlVVdRR1BPZyUzRCUzRA..")
    element_wait = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.NAME, 'e')))
    # browser.implicitly_wait(1000)

    # Login Credentials
    login_Credentials = browser.find_element(By.NAME, 'e')
    login_Credentials.send_keys('sxm9759@mavs.uta.edu')
    time.sleep(3)

    submit = browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/form/div[2]')
    submit.click()
    time.sleep(3)

    password = browser.find_element(By.NAME, 'p')
    password.send_keys('Edenhazard1!')
    time.sleep(3)

    submit_pass = browser.find_element(By.CLASS_NAME, 'LoginPasswordForm-loginButton')
    submit_pass.click()
    time.sleep(5)

    # Second Window since the login is authenticated, browser sessions is authenticated.
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[1])
    browser.get('https://app.asana.com/0/goals/1205772404764116/list?v=1.0&view_mode=domain_level')
    element_search = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'PrimaryButton')))

    # Finding Goal and Adding Goals in this case its TestGoal3.
    goals_add = browser.find_element(By.CLASS_NAME, 'PrimaryButton')
    goals_add.click()
    time.sleep(4)

    goal_btn = browser.find_element(By.CLASS_NAME, 'MenuItemA11y')
    goal_btn.click()
    time.sleep(3)

    goal_text = browser.find_element(By.CLASS_NAME, 'TextInputBase')
    goal_text.send_keys('TestGoal3')
    time.sleep(2)

    goal_save_btn = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[2]')
    goal_save_btn.click()

    time.sleep(3)

    text_area = browser.find_element(By.CLASS_NAME, 'simpleTextarea')

    assert "TestGoal3" in text_area.text
    print(text_area.text)
    print("Test Case Pass")

    time.sleep(3)

if __name__ == "__main__":
    pytest.main([__file__])