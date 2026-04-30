from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.last.fm/charts/weekly?page=1")
time.sleep(5)
rows = driver.find_elements(By.CSS_SELECTOR, ".weeklychart-item")
rising = []
falling = []

for row in rows:
    artist = row.find_element(By.CSS_SELECTOR, ".weeklychart-name").text
    listeners = row.find_element(By.CSS_SELECTOR, ".weeklychart-listeners").text
    scrobblers = row.find_element(By.CSS_SELECTOR, ".weeklychart-scrobblers").text
    change = row.find_element(By.CSS_SELECTOR, ".weeklychart-change").text
    if "up".title() in change:
        rising.append((artist, listeners, scrobblers))
    elif "down".title() in change:
        falling.append((artist, listeners, scrobblers))

with open("rising.txt", "w") as f:
    for item in rising:
        f.write(f"{item[0]} - {item[1]} - {item[2]}\n")

with open("falling.txt", "w") as f:
    for item in falling:
        f.write(f"{item[0]} - {item[1]} - {item[2]}\n")
print(rising, falling)

driver.quit()