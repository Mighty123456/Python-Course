import requests
from bs4 import BeautifulSoup

for page in range(1, 4):
    print(f"\n--- PAGE {page} ---")
    url = f"https://quotes.toscrape.com/page/{page}/"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    quotes = soup.find_all("span", class_="text")

    for q in quotes:
        print(q.text)
