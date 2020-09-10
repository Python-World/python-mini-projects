from bs4 import BeautifulSoup
import requests
import re

#Function to get Movie Details
def getMovieDetails(movieName):
    #Base URL of IMDB website
    url='https://www.imdb.com'

    #Query to find movie title 
    query='/find?q='

    #Empty dictionary to store movie Details
    movieDetails={}
    
    #Query formed
    movienamequery=query+'+'.join(movieName.strip().split(' '))

    #WebPage is obtained and parsed
    html=requests.get(url+movienamequery)
    bs=BeautifulSoup(html.text,'html.parser')

    #Gets the first movie that appears in title section    
    result=bs.findAll('a',{'href':re.compile('^/title/.+$')})

    if result==[]:
        return None

    result=result[1]
    movielink=url+result.attrs['href']
    movieDetails['name']=result.text

    #Gets the page with movie details
    html=requests.get(movielink)
    bs=BeautifulSoup(html.text,'html.parser')
    #Year
    movieDetails['year']=bs.find('span',{'id':'titleYear'}).a.text

    subtext=bs.find('div',{'class':'subtext'})

    #Rating,Genres,Runtime,Release Date,
    movieDetails['rating']=bs.find('div',{'class':'ratingValue'}).span.text
    movieDetails['genres']=[i.text for i in subtext.findAll('a',{'title':None})]
    movieDetails['runtime']=subtext.time.text.strip()
    movieDetails['release_date']=subtext.find('a',{'title':'See more release dates'}).text.strip()

    #Gets the credit section of the page
    creditSummary=bs.findAll('div',{'class':'credit_summary_item'})

    #Directors,Writers and Cast
    movieDetails['directors']=[i.text for i in creditSummary[0].findAll('a')]
    movieDetails['writers']=[i.text for i in creditSummary[1].findAll('a') if 'name' in i.attrs['href'] ]
    movieDetails['cast']=[i.text for i in creditSummary[2].findAll('a') if 'name' in i.attrs['href']]

    #The plot is seperate AJAX call and does not come in the html page, So one more request to plotsummary page
    html=requests.get(movielink+'plotsummary')
    bs=BeautifulSoup(html.text,'html.parser')
    
    #Plot
    movieDetails['plot']=bs.find('li',{'class':'ipl-zebra-list__item'}).p.text.strip()

    #Returns the dictionary with movie details
    return movieDetails


if __name__ == "__main__":
    movieName=input('Enter the movie name whose details are to be fetched\n')
    movieDetails=getMovieDetails(movieName)
    if movieDetails is None:
        print('No movie of this name found !!!!!')
        quit()
    print('{movie} ({year})'.format(movie=movieDetails['name'],year=movieDetails['year']))
    print('Rating:',movieDetails['rating'])
    print('Runtime:',movieDetails['runtime'])
    print('Release Date',movieDetails['release_date'])
    print('Genres:',', '.join(movieDetails['genres']))
    print('Director:',', '.join(movieDetails['directors']))
    print('Writer:',', '.join(movieDetails['writers']))
    print('Cast:',', '.join(movieDetails['cast']))
    print('Plot Summary:\n',movieDetails['plot'])
