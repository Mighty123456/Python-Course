import requests
from bs4 import BeautifulSoup

url = "https://example.com"
html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")

print("All Headings:")
for i in range(1, 7):
    for heading in soup.find_all(f"h{i}"):
        print(heading.text)

print("\nAll Paragraphs:")
for p in soup.find_all("p"):
    print(p.text)
