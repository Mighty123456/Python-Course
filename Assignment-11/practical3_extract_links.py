import requests
from bs4 import BeautifulSoup

url = "https://example.com"
html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")

links = soup.find_all("a")

for link in links:
    print("Text:", link.text)
    print("URL:", link.get("href"))
    print("-" * 50)
