import requests
from bs4 import BeautifulSoup
import os

url = "https://www.wikipedia.org"
html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")

os.makedirs("images", exist_ok=True)

for img in soup.find_all("img"):
    src = img.get("src")
    if not src.startswith("http"):
        src = "https:" + src

    img_data = requests.get(src).content

    name = src.split("/")[-1]

    with open("images/" + name, "wb") as f:
        f.write(img_data)

    print("Downloaded:", name)
