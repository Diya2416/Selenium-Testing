from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open homepage
driver.get("https://the-internet.herokuapp.com")
time.sleep(2)

# Find all anchor tags
links = driver.find_elements(By.TAG_NAME, "a")

valid_link_count = 0

print("Extracted Hyperlinks:")
print("----------------------------------------")

# Loop through each link
for link in links:
    link_text = link.text.strip()
    href = link.get_attribute("href")

    # Skip if href contains 'javascript'
    if href and "javascript" in href.lower():
        continue

    # Print only if text is not empty
    if link_text != "" and href:
        print("Link Text:", link_text)
        print("URL:", href)
        print("----------------------------------------")
        valid_link_count += 1

# Print total count
print("Total Valid Links Found:", valid_link_count)

time.sleep(3)
driver.quit()
