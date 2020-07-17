import requests
from bs4 import BeautifulSoup
import lxml

#defining variables and url
title= str(input("Enter the title of movie/series: ")).lower()
release= str(input("Enter the year of release: ")).lower()
query='+'.join(title.split())
URL= f'https://www.imdb.com/search/title/?title={query}'

s=requests.session()      #setting up session

try:
    response= s.get(URL) 
    soup= BeautifulSoup(response.content, 'lxml')
    containers=soup.find_all('div', class_='lister-item-content')
    
    for result in containers:
        name= result.h3.a.text.lower()
        year= result.h3.find('span', class_='lister-item-year text-muted unbold').text.lower()

        if title in name and release in year:
            rating= result.find('div', class_='inline-block ratings-imdb-rating')['data-value']
            print(f'Rating of {title}:', rating)
except:
    print("Try again with valid combination of tile and release year")
