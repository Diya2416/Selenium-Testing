from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open website
driver.get("https://the-internet.herokuapp.com/tables")
time.sleep(2)

# Locate Table 1
table = driver.find_element(By.ID, "table1")

# Get all rows (excluding header)
rows = table.find_elements(By.TAG_NAME, "tr")[1:]

high_due = []
low_due = []

total_high_due = 0
total_low_due = 0

highest_due = 0
highest_person = {}

# Nested loop through rows and columns
for row in rows:
    columns = row.find_elements(By.TAG_NAME, "td")

    last_name = columns[0].text
    first_name = columns[1].text
    email = columns[2].text
    due_text = columns[3].text  # Example: $100.00

    # Remove $ and convert to float
    due_amount = float(due_text.replace("$", ""))

    person = {
        "Last Name": last_name,
        "First Name": first_name,
        "Email": email,
        "Due": due_amount
    }

    # Categorize based on due amount
    if due_amount > 50:
        high_due.append(person)
        total_high_due += due_amount
    else:
        low_due.append(person)
        total_low_due += due_amount

    # Check highest due
    if due_amount > highest_due:
        highest_due = due_amount
        highest_person = person

# ----------- OUTPUT SECTION -----------

print("\nHigh Due (> $50):")
for person in high_due:
    print(person)

print("\nLow Due (<= $50):")
for person in low_due:
    print(person)

print("\nTotal High Due Amount: $", total_high_due)
print("Total Low Due Amount: $", total_low_due)

print("\nPerson with Highest Due:")
print(highest_person)

time.sleep(3)
driver.quit()
