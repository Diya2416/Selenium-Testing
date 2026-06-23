from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

# Open Facebook
driver.get("https://www.facebook.com")

wait = WebDriverWait(driver, 10)

# Click "Create New Account"
create_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='open-registration-form-button']"))
)
create_btn.click()

# Wait for registration form to load
wait.until(EC.visibility_of_element_located((By.NAME, "birthday_day")))

# Locate dropdowns
day_dropdown = Select(driver.find_element(By.NAME, "birthday_day"))
month_dropdown = Select(driver.find_element(By.NAME, "birthday_month"))
year_dropdown = Select(driver.find_element(By.NAME, "birthday_year"))

# -------- DAY SELECTION --------
for option in day_dropdown.options:
    if option.text == "15":
        day_dropdown.select_by_visible_text("15")
        print("Day 15 selected")
        break

# -------- MONTH SELECTION --------
month_selected = False
for option in month_dropdown.options:
    if option.text == "May":
        month_dropdown.select_by_visible_text("May")
        print("Month May selected")
        month_selected = True
        break

# If May not found, select Jan
if not month_selected:
    month_dropdown.select_by_visible_text("Jan")
    print("May not found → Jan selected as default")

# -------- YEAR SELECTION --------
selected_year = None

for option in year_dropdown.options:
    year = int(option.text)

    if year > 1990 and year < 2005:
        year_dropdown.select_by_visible_text(option.text)
        selected_year = year
        print("Year selected:", year)
        break

# -------- VALIDATION --------
selected_day = day_dropdown.first_selected_option.text
selected_month = month_dropdown.first_selected_option.text
selected_year = year_dropdown.first_selected_option.text

print("\nFinal Selected Values:")
print("Day:", selected_day)
print("Month:", selected_month)
print("Year:", selected_year)

time.sleep(5)
driver.quit()
