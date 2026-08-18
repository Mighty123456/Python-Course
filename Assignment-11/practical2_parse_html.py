import requests
from bs4 import BeautifulSoup

url = "https://example.com"
html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")

print("Page Title:", soup.title.string)
print("\nAll Paragraphs:\n")

paragraphs = soup.find_all("p")
for p in paragraphs:
    print(p.text)
