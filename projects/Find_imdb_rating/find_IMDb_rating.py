from bs4 import BeautifulSoup
import requests
import json

# Setting up session
s = requests.session()  

#File to write movies into 
file1 = open ("ratings.csv", "w")

with open("movies.txt", "r") as file2:
    for line in file2:
        x = line.split(", ")
        title = x[0].lower()
        release = x[1]
        query = "+".join(title.split())
        URL = "https://www.imdb.com/search/title/?title=" + query
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

                # print(name)
                # print(year)
                # print(release)

                if title in name and release in year:
                    rating = result.find("div",class_="inline-block ratings-imdb-rating")["data-value"]
                    print(f"Rating of {name1}:", rating)
                    genres = []
                    genre = result.p.find("span", class_="genre")
                    for x in genre:
                        genres.append(x)
                    file1.write(name1)
                    file1.write(',')
                    file1.write(rating)
                    # file1.write(',')
                    file1.write('\n')
                    
                    


        except Exception:
            print("Try again with valid combination of tile and release year")

file1.close()
    
