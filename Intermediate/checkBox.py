# Check Box Automation Practice
# Website used: URL- https://dmytro-ch21.github.io

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# open Browser and url page
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://dmytro-ch21.github.io")
time.sleep(2)
button = driver.find_element(By.XPATH, "//a[contains(.,'Go to Dropdowns')]")
button.click()
time.sleep(2)

# Automating checkboxs
checkbox = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
# clicking checkbox using for loop
for field in checkbox:
    if not field.is_selected():
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
radio_btn = driver.find_elements(By.XPATH, "//input[@type='radio']")
# using for loop to automate all radio btn
for radio in radio_btn:
    if not radio.is_selected():
        radio.click()

print("All radio Buttons are automated successfully ")
time.sleep(3)

# signle dropdown automation
dropdownSingle = driver.find_element(By.ID, "carBrands")
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", dropdownSingle)
time.sleep(2)
dropdownSingle.click()
singleSelectOPtion = driver.find_elements(By.TAG_NAME, "option")
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
multiSelect = driver.find_element(By.CLASS_NAME, "select2-search__field")
multiSelect.click()
time.sleep(2)
#  select the car brands from the list
volve = driver.find_element(By.XPATH, "//li[contains(@id,'volvo')]")
volve.click()
time.sleep(1)
multiSelect = driver.find_element(By.CLASS_NAME, "select2-search__field")
multiSelect.click()
audi = driver.find_element(By.XPATH, "//li[contains(@id,'audi')]")
audi.click()
time.sleep(1)
# Removing Volvo from selection
removeVolvo = driver.find_element(By.CSS_SELECTOR, "li[title='Volvo'] span[role='presentation']")
removeVolvo.click()
time.sleep(1)
# Adding mercedes in the list
mercedes = driver.find_element(By.XPATH, "//li[contains(@id,'mercedes')]")
mercedes.click()
time.sleep(1)
# Remove all selected items
removeAll = driver.find_element(By.CLASS_NAME, "select2-selection__clear")
removeAll.click()
time.sleep(2)

# Searchable Dropdown
searchDropdown = driver.find_element(By.XPATH,"//input[@class='search-box']")
searchDropdown.click()
searchDropdown.send_keys("suv")
searchDropdown.send_keys("h")
searchDropdown.send_keys("c")
searchDropdown.send_keys("co")

# Browser closed
driver.quit()
print("Test Executed Successfully ")
