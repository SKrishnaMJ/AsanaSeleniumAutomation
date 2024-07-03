from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

#Intial Intialization
driver = webdriver.Chrome()
driver.get("https://app.asana.com/-/login?_gl=1*1rzaf95*_ga*OTM2MDAxNDgzLjE2OTc4NjIzNjM.*_ga_J1KDXMCQTH*MTY5ODAzOTY2NC4yLjEuMTY5ODA0MDM5NC4wLjAuMA..*_fplc*UThZUlB4NU9NJTJCaENDQml6dG5mUTRHRHZpQ2UyaWNGMllrTlh2aG9udVRWUWFRclJVY2hMJTJGcnR0WW5Qdk9jUURMckd3QzNuUGRVWUQyS09zdmlpWXpkYVdKejBKUm10RndpSWRMNDRaWDdLOFFFZzcxazQxdnNlVVdRR1BPZyUzRCUzRA..")
element_wait = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, 'e')))
driver.implicitly_wait(1000)

#Login Credentials
login_Credentials = driver.find_element(By.NAME, 'e')
login_Credentials.send_keys('sxm9759@mavs.uta.edu')
time.sleep(3)

submit = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/form/div[2]')
submit.click()
time.sleep(3)

password = driver.find_element(By.NAME, 'p')
password.send_keys('Edenhazard1!')
time.sleep(3)

submit_pass = driver.find_element(By.CLASS_NAME, 'LoginPasswordForm-loginButton')
submit_pass.click()
time.sleep(10)

#Second Window since the login is authenticated, broswer sessions is authenticated.
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get('https://app.asana.com/0/goals/1205772404764116/list?v=1.0&view_mode=domain_level')
element_search = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'PrimaryButton')))

#Finding Goal and Adding Goals in this case its TestGoal3.
goals_add = driver.find_element(By.CLASS_NAME, 'PrimaryButton')
goals_add.click()
time.sleep(5)

goal_btn = driver.find_element(By.CLASS_NAME, 'MenuItemA11y')
goal_btn.click()
time.sleep(3)

goal_text= driver.find_element(By.CLASS_NAME,'TextInputBase')
goal_text.send_keys('TestGoal3')
time.sleep(2)

goal_save_btn= driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[2]')
goal_save_btn.click()

time.sleep(3)

text_area=driver.find_element(By.CLASS_NAME,'simpleTextarea')

if "TestGoal3" in text_area:
    print(text_area.text)
    print("Test Case Pass")

time.sleep(3)
driver.quit()