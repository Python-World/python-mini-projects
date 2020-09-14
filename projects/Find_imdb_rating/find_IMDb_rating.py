import requests
import json

# Defining variables and url
title = str(input("Enter the title of movie/series: "))
year = str(input("Enter the year of release: "))
query = "+".join(title.split())

request_link = 'http://www.omdbapi.com/?i=tt3896198&apikey=2c84f11f'

#final request link using OMDb API
request = request_link + '&t=' + query + '&y=' + year

#requesting data from OMBd
response = requests.get(request)

#converting to json (dictionary)
response = response.json()

#printing imdb rating
print(response['imdbRating'])
