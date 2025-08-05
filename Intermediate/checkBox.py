# Check Box Automation Practice
# Website used: URL- https://dmytro-ch21.github.io
from operator import index

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# open Browser and url page
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://dmytro-ch21.github.io")
time.sleep(2)
button = driver.find_element(By.XPATH,"//a[contains(.,'Go to Dropdowns')]")
button.click()
time.sleep(2)
# Automating checkboxs
checkbox = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
# clicking checkbox using for loop
for field in checkbox:
    field.click()

print("All checkbox clicked")
time.sleep(2)
# clicking checkbox through indexing
# checkbox[0].click()
# time.sleep(1)
# checkbox[1].click()
# time.sleep(1)
# checkbox[2].click()
# time.sleep(1)
# checkbox[3].click()
# time.sleep(1)
# checkbox[4].click()
# time.sleep(1)

# Automating all Radio buttons
radio_btn = driver.find_elements(By.XPATH,"//input[@type='radio']")
# using for loop to automate all radio btn
for radio in radio_btn:
    radio.click()

print("All radio Buttons are automated successfully ")
time.sleep(3)

# signle dropdown automation
dropdownSingle = driver.find_element(By.ID,"carBrands")
dropdownSingle.click()
singleSelectOPtion = driver.find_elements(By.TAG_NAME,"option")
singleSelectOPtion[0].click()
time.sleep(1)
singleSelectOPtion[1].click()
time.sleep(1)
singleSelectOPtion[2].click()
time.sleep(1)
singleSelectOPtion[3].click()
time.sleep(2)
print("All dropdown selected Successfully ")

# Multi-Select Dropdown


# Browser closed
driver.quit()
print("Test Executed Successfully ")