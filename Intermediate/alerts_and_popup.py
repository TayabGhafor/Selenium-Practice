# importing required libraries and packages
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# initializing & opening Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()
# opening the website
driver.get("http://uitestingplayground.com/")
time.sleep(2)
alert_page = driver.find_element(By.PARTIAL_LINK_TEXT,"Alerts")
alert_page.click()
time.sleep(1)

# Simple Alert handeling
alert_btn = driver.find_element(By.ID,"alertButton")
alert_btn.click()
time.sleep(2)
alert = driver.switch_to.alert
time.sleep(1)
print("Simple Alert Message:", alert.text)
alert.accept()
time.sleep(2)
print("Simple Alert Passed ✅")

# Confirm Alert handeling
confirm_alert_button = driver.find_element(By.ID,"confirmButton")
confirm_alert_button.click()
time.sleep(1)
# switch focus to confirm alert popup
confirm_alert = driver.switch_to.alert
print("Confirm Alert Message:", confirm_alert.text)
time.sleep(1)
confirm_alert.accept()
time.sleep(2)
# confirming the second popup message
driver.switch_to.alert.accept()
time.sleep(1)
print("Confirm Alert Passed with True Value ✅")

# Confirm Alert with 'cancel' option
confirm_alert_cancel = driver.find_element(By.ID,"confirmButton")
confirm_alert_cancel.click()
time.sleep(1)
# switch focus to confirm alert popup
confirm_cancel = driver.switch_to.alert
print("Confirm Alert Message:", confirm_cancel.text)
time.sleep(1)
confirm_cancel.dismiss()
time.sleep(2)
# confirming the second popup message
driver.switch_to.alert.accept()
time.sleep(1)
print("Confirm Alert Passed with False Value ✅")


# Prompt Alert Message Handeling
prompt_alert_button = driver.find_element(By.ID,"promptButton")
prompt_alert_button.click()
time.sleep(2)
# switch focus to prompt alert popup
prompt_alert = driver.switch_to.alert
print("Prompt Alert Message:", prompt_alert.text)
time.sleep(1)
prompt_alert.send_keys("Tayab Malik")
time.sleep(2)
prompt_alert.accept()
time.sleep(2)
# confirming the second popup message
prompt_alert.accept()
time.sleep(1)
print("Prompt Alert Passed ✅")

# back to the Homepage
back_to_home = driver.find_element(By.PARTIAL_LINK_TEXT,"Home")
back_to_home.click()
time.sleep(1)

# closing the Browser
print("All Test Passed ✅")
time.sleep(1)
driver.quit()