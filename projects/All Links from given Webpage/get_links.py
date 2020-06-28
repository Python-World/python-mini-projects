import requests as rq
from bs4 import BeautifulSoup

url = input("Enter Link")
data = rq.get(url)
soup = BeautifulSoup(data.text, "html.parser")
links = []
for link in soup.find_all("a"):
    links.append(link.get("href"))

print(links[:10])
