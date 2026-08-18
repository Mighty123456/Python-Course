from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup browser
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open website
driver.get("https://quotes.toscrape.com/")
driver.maximize_window()
time.sleep(2)

# Extract quotes and authors
quotes = driver.find_elements(By.CLASS_NAME, "text")
authors = driver.find_elements(By.CLASS_NAME, "author")

print("\n--- DATA EXTRACTED USING SELENIUM ---\n")
for i in range(len(quotes)):
    print(f"Quote {i+1}: {quotes[i].text}")
    print(f"Author: {authors[i].text}")
    print("-" * 40)

# Close browser
driver.quit()
