from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

def test_login(username, password):
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Wait for message
    wait = WebDriverWait(driver, 10)
    message = wait.until(
        EC.visibility_of_element_located((By.ID, "flash"))
    ).text

    if "You logged into a secure area!" in message:
        print("Login Successful")
    else:
        print("Login Failed")
        print("Error Message:", message)

# ✅ Valid credentials
test_login("tomsmith", "SuperSecretPassword!")

# ❌ Invalid credentials
test_login("wronguser", "wrongpass")

driver.quit()
