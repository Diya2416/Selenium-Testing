from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/dynamic_controls")

try:
    remove_button = driver.find_element(By.XPATH, "//button[text()='Remove']")
    remove_button.click()

    time.sleep(3)

    try:
        checkbox = driver.find_element(By.ID, "checkbox")

        if checkbox.is_displayed():
            print("Checkbox exists")

    except NoSuchElementException:
        print("Checkbox removed")

        message = driver.find_element(By.ID, "message").text
        print("Confirmation Message:", message)

except Exception as e:
    print("Error occurred:", e)

finally:
    time.sleep(2)
    driver.quit()
