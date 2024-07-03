# This Code tests (i) If the Search bar is accessible (ii) If the advanced search button can be clicked (iii) If the advanced search bar can be populated (iv) Displays the page contents

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://app.asana.com/-/login?_gl=1*1rzaf95*_ga*OTM2MDAxNDgzLjE2OTc4NjIzNjM.*_ga_J1KDXMCQTH*MTY5ODAzOTY2NC4yLjEuMTY5ODA0MDM5NC4wLjAuMA..*_fplc*UThZUlB4NU9NJTJCaENDQml6dG5mUTRHRHZpQ2UyaWNGMllrTlh2aG9udVRWUWFRclJVY2hMJTJGcnR0WW5Qdk9jUURMckd3QzNuUGRVWUQyS09zdmlpWXpkYVdKejBKUm10RndpSWRMNDRaWDdLOFFFZzcxazQxdnNlVVdRR1BPZyUzRCUzRA..")
element_wait = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, 'e')))
driver.implicitly_wait(1000)

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

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get('https://app.asana.com/0/home/1205772404764116')
element_search = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME,'TopbarSearchInputButton-baseButton')))



search_btn= driver.find_element(By.CLASS_NAME,'TopbarSearchInputButton-baseButton')
search_btn.click()

search1 = driver.find_element(By.CLASS_NAME,'TypeaheadActionItemStructure-text')
search1.click()
time.sleep(3)

advanced_search = driver.find_element(By.CLASS_NAME,'SearchTextInput')
advanced_search.send_keys("Tasks")
time.sleep(3)

prim_btn = driver.find_element(By.CLASS_NAME,'PrimaryButton')
prim_btn.click()
time.sleep(3)

page_content = driver.find_element(By.CLASS_NAME,'Scrollable')
print(page_content.text)
time.sleep(3)



time.sleep(3)
driver.quit()


