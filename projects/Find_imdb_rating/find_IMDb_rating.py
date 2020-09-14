import requests
from bs4 import BeautifulSoup

# Defining variables and url
title = str(input("Enter the title of movie/series: "))
release = str(input("Enter the year of release: "))
query = "+".join(title.split())
#RL = f"https://www.imdb.com/search/title/?title={query}"

request_link = 'http://www.omdbapi.com/?i=tt3896198&apikey=2c84f11f'

#api_key = 2c84f11f

request = request_link + '&t=' + query
result = requests.get(request)

print(result.text)

# s = requests.session()  # Setting up session

# try:
#     response = s.get(URL)
#     soup = BeautifulSoup(response.content, features="lxml")
#     containers = soup.find_all("div", class_="lister-item-content")

#     for result in containers:
#         name = result.h3.a.text.lower()
#         year = result.h3.find(
#             "span", class_="lister-item-year text-muted unbold"
#         ).text.lower()

#         if title in name and release in year:
#             rating = result.find("div",
#                                  class_="inline-block ratings-imdb-rating")[
#                                  "data-value"]
#             print(f"Rating of {name}:", rating)
# except Exception:
#     print("Try again with valid combination of tile and release year")
