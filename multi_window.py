from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open website
driver.get("https://the-internet.herokuapp.com/windows")
time.sleep(2)

# Store parent window handle
parent_window = driver.current_window_handle
print("Parent Window Handle:", parent_window)

# Click "Click Here" 3 times
for i in range(3):
    driver.find_element(By.LINK_TEXT, "Click Here").click()
    time.sleep(1)

# Get all window handles
all_windows = driver.window_handles
print("\nTotal Windows Opened:", len(all_windows))

extracted_texts = []
closed_count = 0

# Loop through all windows
for handle in all_windows:
    driver.switch_to.window(handle)
    title = driver.title

    print("\nWindow Handle:", handle)
    print("Window Title:", title)

    # Check if this is a child window
    if "New Window" in title:
        text = driver.find_element(By.TAG_NAME, "h3").text
        extracted_texts.append(text)
        print("Extracted Text:", text)

# Switch back to parent window
driver.switch_to.window(parent_window)
print("\nSwitched back to Parent Window")

# Close all child windows
for handle in all_windows:
    if handle != parent_window:
        driver.switch_to.window(handle)
        driver.close()
        closed_count += 1

# Switch back to parent again
driver.switch_to.window(parent_window)

print("\nChild Windows Closed:", closed_count)
print("Parent Window Still Active:", driver.title)

print("\nTotal Windows Opened:", len(all_windows))
print("Total Windows Closed:", closed_count)

time.sleep(3)
driver.quit()
