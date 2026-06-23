from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# Start browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open website
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

time.sleep(2)

# Click Start button
driver.find_element(By.CSS_SELECTOR, "#start button").click()

max_attempts = 10
attempt = 0
element_found = False

# Retry mechanism using while loop
while attempt < max_attempts:
    try:
        element = driver.find_element(By.ID, "finish")

        # Check if element is visible
        if element.is_displayed():
            print("Element appeared!")
            print("Text Content:", element.text)
            element_found = True
            break

    except NoSuchElementException:
        pass  # Element not found yet

    attempt += 1
    print(f"Attempt {attempt}: Element not visible yet")
    time.sleep(1)

# After loop check
if not element_found:
    print("\nElement not found after", attempt, "attempts")

else:
    print("\nElement found after", attempt + 1, "attempt(s)")

time.sleep(3)
driver.quit()
