from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Start browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open website
driver.get("https://the-internet.herokuapp.com/dropdown")
time.sleep(2)

# Locate dropdown
dropdown_element = driver.find_element(By.ID, "dropdown")

# Create Select object
dropdown = Select(dropdown_element)

# Get all options
options = dropdown.options

enabled_count = 0

print("Dropdown Options:")
print("-----------------------------------")

# Loop through each option
for option in options:
    option_text = option.text

    # Check if option is enabled
    if option.is_enabled():
        enabled_count += 1

        # Select specific options
        if option_text == "Option 1" or option_text == "Option 2":
            dropdown.select_by_visible_text(option_text)
            print(f"{option_text} selected successfully")
            time.sleep(1)
    else:
        print(f"{option_text} → Option is disabled")

# Display total enabled options
print("-----------------------------------")
print("Total Enabled Options:", enabled_count)

time.sleep(3)
driver.quit()
