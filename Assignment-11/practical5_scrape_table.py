import requests
from bs4 import BeautifulSoup

url = "https://www.w3schools.com/html/html_tables.asp"
html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")

table = soup.find("table", id="customers")

rows = table.find_all("tr")

for row in rows:
    cols = row.find_all(["td", "th"])
    cols = [c.text.strip() for c in cols]
    print(cols)
