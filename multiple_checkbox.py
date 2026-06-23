from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open website
driver.get("https://the-internet.herokuapp.com/checkboxes")
time.sleep(2)

# Locate all checkboxes
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

print("Total Checkboxes Found:", len(checkboxes))
print("-----------------------------------")

# Loop through each checkbox
for index, checkbox in enumerate(checkboxes, start=1):

    if checkbox.is_selected():
        print(f"Checkbox {index}: Already checked")
    else:
        checkbox.click()
        print(f"Checkbox {index}: Was not checked → Now selected")

# Verify final status
print("\nFinal Status of Checkboxes:")
print("-----------------------------------")

for index, checkbox in enumerate(checkboxes, start=1):
    if checkbox.is_selected():
        print(f"Checkbox {index}: Selected")
    else:
        print(f"Checkbox {index}: Not Selected")

time.sleep(3)
driver.quit()
