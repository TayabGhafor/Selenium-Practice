# This the is about the navigation concept
#  For Example
# Step 1 - Open chrome browser
# Step 2 - Navigate to google
# Step 3 - Navigate to Youtube
# Step 4 - Navigate back to Google
# Step 5 - Navigate forward to Youtube
# Step 6 - Refresh the current page (Youtube)
# Step 7 - Close the Chrome Browser

from selenium import webdriver
import time

#opening the chrome
driver = webdriver.Chrome()
print("Browser opened Successfully ✅ \n")

# Navigating to the Google
driver.get("https://www.google.com")
time.sleep(2)     # Wait for 2sec for the proper load of page
print("Navigate to google Successfully ✅ \n")

# Navigating to the Youtube
driver.get("https://www.youtube.com")
time.sleep(2)      # Wait for 2sec for the proper load of page
print("Navigate to youtube Successfully ✅ \n")

# Navigating back to Google
driver.back()
time.sleep(1)
print("Navigate back to google Successfully ✅ \n")

# Navigating Froward to Youtube
driver.forward()
time.sleep(1)
print("Navigate forward to youtube Successfully ✅ \n")

# Refreshing the current page (Youtube)
driver.refresh()
time.sleep(2)
print("Current page (Youtube) Refreshed Successfully ✅ \n")

# Closing the Browser
driver.quit()
print("Browser closed Successfully ✅ \n")