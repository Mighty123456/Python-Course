from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def facebook_auto_post():

    phone = "9510610346"
    password = "#Ansh@13032005#"
    post_text = "This is an automated post using Selenium!"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    driver.get("https://www.facebook.com/")

    # Enter phone number
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "email"))
    ).send_keys(phone)

    # Enter password
    driver.find_element(By.ID, "pass").send_keys(password)

    # Click Login
    driver.find_element(By.NAME, "login").click()

    print("✔ Login clicked. Please complete Meta verification manually.")
    input("⏳ After verification is finished, press ENTER to continue...")

    # Wait until homepage loads (FB top bar visible)
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='Create a post']"))
    )

    print("✔ Login successful. Now creating post...")

    # Click "What's on your mind?"
    driver.find_element(By.CSS_SELECTOR, "[aria-label='Create a post']").click()

    # Wait for post text area
    textarea = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='textbox']"))
    )
    textarea.send_keys(post_text)

    # Click Post button
    post_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Post']"))
    )
    post_button.click()

    print("🎉 Post published successfully!")

facebook_auto_post()
