from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

# Setting up session
s = requests.session()  

#File to write movies into 

films = ['Star Wars: Episode V - The Empire Strikes Back', 'The wolf of wall street', 'Shutter Island']

names = []
ratings = []
genres = []

for line in films:
    # x = line.split(", ")
    title = line.lower()
    # release = x[1]
    query = "+".join(title.split()) 
    URL = "https://www.imdb.com/search/title/?title=" + query
    print(URL)
    # print(release)
    try: 
        response = s.get(URL)

        #getting contect from IMDB Website
        content = response.content

        # print(response.status_code)

        soup = BeautifulSoup(response.content, features="html.parser") 
        #searching all films containers found
        containers = soup.find_all("div", class_="lister-item-content")
        for result in containers:
            name1 = result.h3.a.text
            name = result.h3.a.text.lower()

            # Uncomment below lines if you want year specific as well, define year variable before this 
            # year = result.h3.find(
            # "span", class_="lister-item-year text-muted unbold"
            # ).text.lower() 

            #if film found (searching using name)
            if title in name:
                #scraping rating
                rating = result.find("div",class_="inline-block ratings-imdb-rating")["data-value"]
                # print(f"Rating of {name1}:", rating)
                #scraping genre
                genre = result.p.find("span", class_="genre")
                genre = genre.contents[0]

                #appending name, rating and genre to individual lists
                names.append(name1)
                ratings.append(rating)
                genres.append(genre)
                


    except Exception:
        print("Try again with valid combination of tile and release year")

#storing in pandas dataframe
df = pd.DataFrame({'Film Name':names,'Rating':ratings,'Genre':genres}) 

#making csv using pandas
df.to_csv('products.csv', index=False, encoding='utf-8')
