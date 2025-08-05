# Multiple Locators using find elements method
# we can use find elements method on following
#  1 - find elements by Name
#  2 - find elements by TagName
#  3 - By Classname
#  4 - BY XPATH
#  5 - BY Link text
#  6 - By partial link text
#  7 - By CSS Selectors

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# opening browser
driver = webdriver.Chrome()
driver.maximize_window()
print("Browser opened Successfully ✅ \n")
# Navigating to the Saucedemo website
driver.get("https://www.saucedemo.com")
time.sleep(4)
print("Navigate to Saucedemo Successfully ✅ \n")

# locating by TagName
Input_Fields = driver.find_elements(By.TAG_NAME,"input")
print(len(Input_Fields))
# finding the index of password and username from the input_fields list
print(Input_Fields[0].get_attribute("id"))
print(Input_Fields[1].get_attribute("id"))
print(Input_Fields[2].get_attribute("id"))
# finding these index using for loop
index = 0
for field in Input_Fields:
    print(f"Index:{index}: {field.get_attribute('id')}")
    index = index + 1

# now entering values of username & password fields
Input_Fields[0].send_keys("standard_user")
Input_Fields[1].send_keys("secret_sauce")
time.sleep(2)
Input_Fields[2].click()
print("User Logged-In Successfully ✅ ")
time.sleep(2)

# List all the Products using find elements & for loop
products = driver.find_elements(By.XPATH,"//div[@data-test='inventory-item-name']")
print("Product List")

for product in products:
    print(product.text)


# close the browser
driver.quit()
print("Browser closed Successfully ✅ ")
print("Overall test Passed ✅ ")