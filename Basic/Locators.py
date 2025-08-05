# This is about the Locators concept in selenium we can locate elements by different means like;
# 1 - Locate element by ID
# 2 - Locate element by Name
# 3 - Locate element by Class Name
# 4 - Locate element by Xpath , etc

# The practical implementation is given below.
# 1- Locate element by ID :

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

# locating element by Name,ID,Xpath,Partial-text,Indexing,Tag Name, and storing it into a username variable
# username = driver.find_element(By.NAME, "user-name")
# username = driver.find_element(By.XPATH,"//input[@id='user-name' and @type='text']")
# username = driver.find_element(By.XPATH,"(//input)[1]")
# username = driver.find_element(By.TAG_NAME,"input")

# using TagName by CSS Selectors
# username = driver.find_element(By.CSS_SELECTOR,"input")

# using ID by CSS selector
username = driver.find_element(By.CSS_SELECTOR,"#user-name")
# entering the username in the input field
username.send_keys("standard_user")
time.sleep(2)
print("Username entered Successfully ✅ \n")

# locating the element by Name,ID,Xpath,Partial-text and storing it into Password variable
# password = driver.find_element(By.ID, "password")
# password = driver.find_element(By.XPATH,"//input[@name='password']")
# by using Attribute through CSS Selectors
password = driver.find_element(By.CSS_SELECTOR,"input[type='password']")
# entering the password in the input field
password.send_keys("secret_sauce")
time.sleep(2)
print("Password entered Successfully ✅ \n")

# CLICKING THE LOGIN button using relative Xpath,by className,
# login = driver.find_element(By.XPATH, "//input[@id='login-button']")
# login = driver.find_element(By.CLASS_NAME,"btn_action")

# By CSS Selectors Class
# login = driver.find_element(By.CSS_SELECTOR,".btn_action")
# By CSS Selector Combination (tagname.classname etc.)
# login = driver.find_element(By.CSS_SELECTOR,"input.btn_action")
# By CSS Selector Parent > Child
#login = driver.find_element(By.CSS_SELECTOR,"form > input[value='Login']")
# BY CSS Selector using Decendent
login = driver.find_element(By.CSS_SELECTOR,"form input.btn_action")
login.click()
time.sleep(2)
print("Logged-In Successfully ✅ \n")

# # Add to cart and item using partial-xpath for the add to cart button
# addToCart = driver.find_element(By.XPATH,"//button[contains(@id,'cart-sauce-labs-fleece-jacket')]")
# addToCart.click()
# time.sleep(4)
# print(" Item added to Cart Successfully ✅ \n")
#
# # Remove item from add to cart
# removeAddToCart = driver.find_element(By.XPATH,"//button[contains(@id,'remove-sauce-labs-fleece')]")
# removeAddToCart.click()
# time.sleep(4)
# print(" Item Removed from add-to-Cart Successfully ✅ \n")

# opening the product details using text,text link,partial link-text locators.
# product = driver.find_element(By.XPATH,"//div[text()='Sauce Labs Bike Light']")
# product = driver.find_element(By.LINK_TEXT,"Sauce Labs Bike Light")
productlink = driver.find_element(By.PARTIAL_LINK_TEXT,"Bike")
productlink.click()
time.sleep(2)
print("Product details opened ✅")

# Add to cart and item using partial-xpath for the add to cart button
addToCart = driver.find_element(By.XPATH,"//button[contains(text(),'to cart')]")
addToCart.click()
time.sleep(2)
print(" Item added to Cart Successfully ✅ \n")

# back to products using relative-xpath with text() function
backToProducts = driver.find_element(By.XPATH,"//button[text()='Back to products']")
backToProducts.click()
time.sleep(2)
print("Back to products Item Successfully ✅ \n")

# open cart using partial-xpath
openCart = driver.find_element(By.XPATH,"//a[contains(@class,'cart_link')]")
openCart.click()
time.sleep(4)
print(" Cart opened Successfully ✅ \n")

# close the browser
driver.quit()
print("Browser closed Successfully ✅ \n")
print("Overall test Passed ✅ \n")