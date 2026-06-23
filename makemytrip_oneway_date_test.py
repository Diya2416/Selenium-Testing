from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from datetime import datetime
import time

# ----------------- Setup ChromeDriver -----------------
service = Service("chromedriver.exe")  # Make sure chromedriver.exe is in same folder
driver = webdriver.Chrome(service=service)
driver.maximize_window()
wait = WebDriverWait(driver, 15)

# ----------------- Open MakeMyTrip -----------------
driver.get("https://www.makemytrip.com")

# ----------------- Close Login Popup -----------------
try:
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@data-cy='closeModal']"))).click()
except:
    pass

# ----------------- Select One Way Trip -----------------
one_way = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@data-cy='oneWayTrip']")))
driver.execute_script("arguments[0].click();", one_way)

# ----------------- Enter From City -----------------
from_city_input = wait.until(EC.element_to_be_clickable((By.ID, "fromCity")))
from_city_input.click()
from_input_box = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='From']")))
from_input_box.clear()
from_input_box.send_keys("Delhi")
wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Delhi, India')]"))).click()

# ----------------- Enter To City -----------------
to_city_input = driver.find_element(By.ID, "toCity")
to_city_input.click()
to_input_box = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='To']")))
to_input_box.clear()
to_input_box.send_keys("Mumbai")
wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Mumbai, India')]"))).click()

# ----------------- Open Calendar -----------------
driver.find_element(By.XPATH, "//span[@data-cy='departureDate']").click()

today = datetime.today()
dates = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class,'DayPicker-Day')]")))

selected_date = None

# ----------------- Iterate Through Dates -----------------
for date in dates:
    classes = date.get_attribute("class")
    if "DayPicker-Day--disabled" in classes:
        continue  # skip disabled dates

    aria_label = date.get_attribute("aria-label")
    if aria_label:
        date_obj = datetime.strptime(aria_label, "%a %b %d %Y")

        # Skip today's date
        if date_obj.date() == today.date():
            print("Today's date skipped – same day booking not preferred")

        # Print weekends
        elif date_obj.weekday() in [5, 6]:  # Saturday=5, Sunday=6
            print("Weekend date found:", date_obj.strftime("%d-%m-%Y"))

        # Select 15th of current month
        elif date_obj.day == 15 and date_obj.month == today.month:
            driver.execute_script("arguments[0].click();", date)
            selected_date = date_obj
            print("Departure date selected:", date_obj.strftime("%d-%m-%Y"))
            break

time.sleep(2)

# ----------------- Verify Selected Date -----------------
selected_value = driver.find_element(By.XPATH, "//span[@data-cy='departureDate']").text
expected_value = selected_date.strftime("%d %b %Y") if selected_date else ""

if selected_date and selected_value:
    if expected_value in selected_value:
        print("Date verification passed")
    else:
        print(f"Date mismatch detected – Expected: {expected_value}, Found: {selected_value}")
else:
    print("No date selected or date not found")

time.sleep(3)
driver.quit()