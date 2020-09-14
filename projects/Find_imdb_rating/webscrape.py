from bs4 import BeautifulSoup
import requests

# Defining variables and url
title = str(input("Enter the title of movie/series: ")).lower()
release = str(input("Enter the year of release: ")).lower()
query = "+".join(title.split())
URL = "https://www.imdb.com/search/title/?title=" + query

print(URL)

s = requests.session()  # Setting up session

file1 = open ("ratings.csv", "a")

try: 
    response = s.get(URL)

    content = response.content

    soup = BeautifulSoup(response.content)
    containers = soup.find_all("div", class_="lister-item-content")
    for result in containers:
        name1 = result.h3.a.text
        name = result.h3.a.text.lower()
        # print(name)
        year = result.h3.find(
            "span", class_="lister-item-year text-muted unbold"
        ).text.lower()

        if title in name and release in year:
            rating = result.find("div",class_="inline-block ratings-imdb-rating")["data-value"]
            print(f"Rating of {name1}:", rating)
            file1.write(name1)
            file1.write(',')
            file1.write(rating)
            file1.write('\n')
            genre = result.p.find("span", class_="genre")
            for x in genre:
                print(x)

except Exception:
    print("Try again with valid combination of tile and release year")

file1.close()