from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://dmytro-ch21.github.io/")
driver.maximize_window()
time.sleep(2)

go_to_dropdown = driver.find_element(By.PARTIAL_LINK_TEXT,"Dropdowns")
go_to_dropdown.click()
time.sleep(2)

# CheckBox

ford_checkbox = driver.find_element(By.ID,"option1")
if not ford_checkbox.is_selected():
    ford_checkbox.click()
else:
    print("ford checked already")
time.sleep(1)

bmw_checkbox = driver.find_element(By.ID,"option2")
if not bmw_checkbox.is_selected():
    bmw_checkbox.click()

checkboxs = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for checkbox in checkboxs:
    if not checkbox.is_selected():
        time.sleep(0.5)
        checkbox.click()

# Radio-Buttons

radio_buttons = driver.find_elements(By.XPATH,"//input[@type='radio']")
for radio in radio_buttons:
    if not radio.is_selected():
        time.sleep(1)
        radio.click()
print("All Radio-Buttons are Checked ✅")

# Single-Select DropDown
single_dropdown = Select(driver.find_element(By.ID,"carBrands"))
single_dropdown.select_by_visible_text("Volvo")
time.sleep(1)
single_dropdown.select_by_visible_text("Saab")
time.sleep(1)
single_dropdown.select_by_visible_text("Audi")
time.sleep(1)
single_dropdown.select_by_visible_text("Mercedes")
print("Single Select Dropdown ✅")

# Multi-Select Dropdown
multi_dropdown = driver.find_element(By.XPATH,"//input[@placeholder='Choose car brands']")
multi_dropdown.click()
dropdown_volvo = driver.find_element(By.XPATH,"//li[contains(@id, 'volvo')]")
dropdown_volvo.click()
time.sleep(1)
multi_dropdown.click()
dropdown_saab = driver.find_element(By.XPATH,"//li[contains(@id, 'saab')]")
dropdown_saab.click()
time.sleep(1)
multi_dropdown.click()
dropdown_audi = driver.find_element(By.XPATH,"//li[contains(@id, 'audi')]")
dropdown_audi.click()
time.sleep(1)
# Remove a single Item
remove_one = driver.find_element(By.XPATH,"(//span[contains(@class, 'choice__remove')])[1]")
remove_one.click()
print("The First selected car item removed from the list ✅")
time.sleep(1)
#remove all selection
clear_selection = driver.find_element(By.XPATH,"//span[@title='Remove all items']")
clear_selection.click()
print("All item removed ✅")
time.sleep(1)

# Custom-Dropdown
custom_dropdown = driver.find_element(By.ID,"custom-select")
driver.execute_script("arguments[0].scrollIntoView(true);",custom_dropdown)
time.sleep(3)
custom_dropdown.click()
time.sleep(1)
# Selecting Blue Option
optionBlue = driver.find_element(By.XPATH,"//div[contains(text(), 'Blue')]")
optionBlue.click()
time.sleep(1)
# Selecting the Red Option
custom_dropdown.click()
optionRed = driver.find_element(By.XPATH,"//div[contains(text(), 'Red')]")
optionRed.click()
time.sleep(1)
print("All Custom Dropdown Tests Passed ✅")

# Searchable Dynamic Dropdown
dynamin_dropdown = driver.find_element(By.CLASS_NAME,"search-box")
dynamin_dropdown.click()
dynamin_dropdown.send_keys("S")
# find option SUV and select it from options
option_SUV = driver.find_element(By.XPATH,"//div[@class='searchable-option' and text()= 'SUV']")
option_SUV.click()
time.sleep(1)

# clearing the existing text in the input field
dynamin_dropdown.clear()
time.sleep(1)
dynamin_dropdown.send_keys("C")

# find option Coupe in the list and select it
option_Coupe = driver.find_element(By.XPATH,"//div[@class='searchable-option' and text()= 'Coupe']")
option_Coupe.click()
time.sleep(1)
print("Searchable Dropdown all test passed ✅")
# back to home-page
back_to_home = driver.find_element(By.LINK_TEXT,"Go Back")
driver.execute_script("arguments[0].scrollIntoView(true);",back_to_home)
time.sleep(2)
back_to_home.click()
time.sleep(1)

# Form Submission Test automation
goto_form = driver.find_element(By.PARTIAL_LINK_TEXT,"Go to Forms")
goto_form.click()
time.sleep(1)
# entering card number
enter_card = driver.find_element(By.ID,"cardNumber")
enter_card.send_keys("1234 5678 9012 3456")
time.sleep(1)
enter_card.clear()
time.sleep(1)
enter_card.send_keys("1234 5678 9012 3456")
# entering CVC Code
enter_cvc = driver.find_element(By.ID,"cvcNumber")
enter_cvc.send_keys("1234 56879")
time.sleep(1)
enter_cvc.clear()
time.sleep(1)
enter_cvc.send_keys("123")
# entering amount
enter_amount = driver.find_element(By.ID,"amount")
enter_amount.send_keys("1000")
time.sleep(1)
#enter First Name
enter_firstname = driver.find_element(By.ID,"firstName")
enter_firstname.send_keys("Tayab")
time.sleep(1)
# enter Last Name
enter_lastname = driver.find_element(By.ID,"lastName")
enter_lastname.send_keys("Malik")
time.sleep(1)
# enter city
enter_city = driver.find_element(By.ID,"city")
enter_city.send_keys("Karachi")
time.sleep(1)
# select state
select_state = Select(driver.find_element(By.ID,"stateSelect"))
select_state.select_by_visible_text("California")
time.sleep(1)
select_state.select_by_visible_text("Florida")
time.sleep(1)
# enter Postal-Code
enter_postal = driver.find_element(By.ID,"postalCode")
enter_postal.send_keys("59066")
time.sleep(1)
# select Payment Option
select_payment = driver.find_element(By.XPATH,"(//input[@type='radio'])[1]")
select_payment.click()
time.sleep(1)
select_payment = driver.find_element(By.XPATH,"(//input[@type='radio'])[3]")
select_payment.click()
time.sleep(1)
# Send a message
send_message = driver.find_element(By.XPATH,"//textarea[@id='floatingTextarea2']")
send_message.click()
send_message.send_keys("Hi There! Bye There")
time.sleep(1)
# Submit the form
send_form = driver.find_element(By.XPATH,"//button[contains(text(),'Send')]")
send_form.click()
time.sleep(2)
print(" Form Submitted Successfully ✅")
# back to home-page
back_to_home = driver.find_element(By.LINK_TEXT,"Go Back")
back_to_home.click()

print("All Test Passed ✅")
time.sleep(2)
driver.quit()