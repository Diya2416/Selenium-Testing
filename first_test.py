from selenium import webdriver
import time

# Launch Chrome browser
driver = webdriver.Chrome()

# Open a website
driver.get("https://www.google.com")

# Print page title
print("Page Title:", driver.title)

# Wait for 5 seconds
time.sleep(5)

# Close the browser
driver.quit()
