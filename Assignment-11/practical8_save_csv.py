import requests
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com"
html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")

quotes = soup.find_all("span", class_="text")

with open("quotes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Quote"])

    for q in quotes:
        writer.writerow([q.text])

print("CSV File Created Successfully!")
