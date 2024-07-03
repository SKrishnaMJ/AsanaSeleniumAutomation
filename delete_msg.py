from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get("https://app.asana.com/-/login?_gl=1*1rzaf95*_ga*OTM2MDAxNDgzLjE2OTc4NjIzNjM.*_ga_J1KDXMCQTH*MTY5ODAzOTY2NC4yLjEuMTY5ODA0MDM5NC4wLjAuMA..*_fplc*UThZUlB4NU9NJTJCaENDQml6dG5mUTRHRHZpQ2UyaWNGMllrTlh2aG9udVRWUWFRclJVY2hMJTJGcnR0WW5Qdk9jUURMckd3QzNuUGRVWUQyS09zdmlpWXpkYVdKejBKUm10RndpSWRMNDRaWDdLOFFFZzcxazQxdnNlVVdRR1BPZyUzRCUzRA..")


ele_wait = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, 'e')))

login = driver.find_element(By.NAME, 'e')
login.send_keys('sxm9759@mavs.uta.edu')
time.sleep(3)

submit = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/form/div[2]')
submit.click()
time.sleep(3)

password = driver.find_element(By.NAME, 'p')
password.send_keys('Edenhazard1!')
time.sleep(3)

submit_pass = driver.find_element(By.CLASS_NAME, 'LoginPasswordForm-loginButton')
submit_pass.click()

time.sleep(5)

# ele_search = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'TopbarSearchInputButton')))

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get('https://app.asana.com/0/inbox/1205772387108322')

btn_wait = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[2]/div/main/div[2]/div/div[1]/div[2]/div[1]/div')))


send_msg_btn = driver.find_element(By.CLASS_NAME, 'PencilPadMiniIcon')
send_msg_btn.click()
time.sleep(5)

inbox_subject = driver.find_element(By.CLASS_NAME,'TextInputBase')
inbox_subject.send_keys('TestSubject by Sai')
time.sleep(3)

inbox_messageTo = driver.find_element(By.CLASS_NAME,'ConversationRecipientsField')
inbox_messageTo.send_keys('sxm9759@mavs.uta.edu')
inbox_messageTo.send_keys(Keys.ENTER)
time.sleep(2)

close_msg = driver.find_element(By.CLASS_NAME,'XIcon')
close_msg.click()
time.sleep(2)

del_msg = driver.find_element(By.CLASS_NAME, 'DangerButton')
del_msg.click()
time.sleep(3)

time.sleep(2)
driver.quit()



