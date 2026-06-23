from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open website
driver.get("https://the-internet.herokuapp.com/status_codes")

time.sleep(2)

# Click on "200" link
driver.find_element(By.LINK_TEXT, "200").click()

time.sleep(2)

# Get page content
page_text = driver.find_element(By.TAG_NAME, "body").text

# Conditional logic
if "200" in page_text:
    print("Success Status")
elif "404" in page_text:
    print("Not Found")
elif "500" in page_text:
    print("Server Error")
else:
    print("Unknown Status")

# Navigate back to main page
driver.back()

time.sleep(2)

print("Returned to main status codes page successfully.")

driver.quit()
