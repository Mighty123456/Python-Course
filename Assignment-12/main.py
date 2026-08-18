from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv


def scrape_quotes():
    # Setup Chrome browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Open website
    url = "https://quotes.toscrape.com/"
    driver.get(url)
    time.sleep(2)

    # Extract quotes
    quotes = driver.find_elements(By.CLASS_NAME, "quote")

    data = []

    for q in quotes:
        text = q.find_element(By.CLASS_NAME, "text").text
        author = q.find_element(By.CLASS_NAME, "author").text
        tags = [t.text for t in q.find_elements(By.CLASS_NAME, "tag")]

        data.append({
            "quote": text,
            "author": author,
            "tags": tags
        })

    # Save to CSV
    with open("quotes.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Quote", "Author", "Tags"])

        for item in data:
            writer.writerow([item["quote"], item["author"], ",".join(item["tags"])])

    # Print to console
    for item in data:
        print("Quote:", item["quote"])
        print("Author:", item["author"])
        print("Tags:", item["tags"])
        print("-" * 40)

    driver.quit()


if __name__ == "__main__":
    scrape_quotes()
