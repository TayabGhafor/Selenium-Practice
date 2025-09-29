# importing libraries
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# initializing Chrome browser
driver = webdriver.Chrome()
# opening the website
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(1)

# logging in to site
inputfields = driver.find_elements(By.TAG_NAME,"input")
inputfields[0].send_keys("standard_user")
inputfields[1].send_keys("secret_sauce")
inputfields[2].click()
time.sleep(5)

# Viewing Product details and adding it to cart
product = driver.find_element(By.PARTIAL_LINK_TEXT,"Backpack")
product.click()
add_to_cart = driver.find_element(By.ID,"add-to-cart")
add_to_cart.click()
time.sleep(1)
back_to_products = driver.find_element(By.ID,"back-to-products")
back_to_products.click()

# Applying Filters
filter_products = driver.find_element(By.XPATH,"//select[@class='product_sort_container']")
filter_products.click()
filter_Option = driver.find_element(By.XPATH,"//option[@value='hilo']")
filter_Option.click()
time.sleep(2)
# adding products to cart
add_to_cart_jacket = driver.find_element(By.ID,"add-to-cart-sauce-labs-fleece-jacket")
add_to_cart_jacket.click()
time.sleep(1)

# Applying Filters
filter_products = driver.find_element(By.XPATH,"//select[@class='product_sort_container']")
filter_products.click()
filter_Option = driver.find_element(By.XPATH,"//option[@value='lohi']")
filter_Option.click()
time.sleep(2)
# adding to cart
add_to_cart_onesie = driver.find_element(By.ID,"add-to-cart-sauce-labs-onesie")
add_to_cart_onesie.click()
time.sleep(1)
# viewing shopping cart
shopping_cart = driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']")
shopping_cart.click()
time.sleep(1)
back_to_shopping = driver.find_element(By.ID,"continue-shopping")
back_to_shopping.click()
time.sleep(1)
# Applying Filters
filter_products = driver.find_element(By.XPATH,"//select[@class='product_sort_container']")
filter_products.click()
filter_Option = driver.find_element(By.XPATH,"//option[@value='za']")
filter_Option.click()
time.sleep(2)
add_to_cart_Tshirt = driver.find_element(By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)")
add_to_cart_Tshirt.click()
time.sleep(1)

# viewing shopping cart
shopping_cart = driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']")
shopping_cart.click()
time.sleep(1)
# removing products from cart
remove_backpack = driver.find_element(By.ID,"remove-sauce-labs-backpack")
remove_backpack.click()
time.sleep(1)
# proceeding to checkout
checkout = driver.find_element(By.ID,"checkout")
checkout.click()
time.sleep(1)
# Adding details for checkout
checkout_inputfields = driver.find_elements(By.TAG_NAME,"input")
checkout_inputfields[0].send_keys("Malik")
checkout_inputfields[1].send_keys("Tayab")
checkout_inputfields[2].send_keys("123456")
time.sleep(2)
# proceed to checkout
continue_checkout = driver.find_element(By.ID,"continue")
continue_checkout.click()
time.sleep(1)

# finish checkout
finish = driver.find_element(By.ID,"finish")
finish.click()
time.sleep(1)
# Back to home
back_home = driver.find_element(By.ID,"back-to-products")
back_home.click()
time.sleep(1)
# interacting with menu
menu = driver.find_element(By.ID,"react-burger-menu-btn")
menu.click()
time.sleep(1)
about = driver.find_element(By.ID,"about_sidebar_link")
about.click()
time.sleep(3)
driver.back()
time.sleep(1)
menu = driver.find_element(By.ID,"react-burger-menu-btn")
menu.click()
time.sleep(1)
reset_app = driver.find_element(By.ID,"reset_sidebar_link")
reset_app.click()
time.sleep(2)

# logout to site
logout = driver.find_element(By.ID,"logout_sidebar_link")
logout.click()
time.sleep(1)
print("All Tests Executed Successfully!")
# closing browser
driver.quit()