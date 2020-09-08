from bs4 import BeautifulSoup
import requests

def getMovieDetails(movieName):
    url='https://www.imdb.com'
    query='/find?q='
    movieDetails={}
    movienamequery=query+movieName.strip().split(' ').join('+')
    html=requests.get(url+movienamequery)
    bs=BeautifulSoup(html.text,'html.parser')
    result=bs.find('td',{'class':'result_text'})
    movielink=url+result.a.attrs['href']
    movieDetails['name']=result.a.text
    html=requests.get(movielink)
    bs=BeautifulSoup(html.text,'html.parser')
    movieDetails['year']=bs.find('span',{'id':'titleYear'}).a.text

    subtext=bs.find('div',{'class':'subtext'})

    movieDetails['rating']=bs.find('div',{'class':'ratingValue'}).span.text
    movieDetails['genres']=[i.text for i in subtext.findAll('a',{'title':None})]
    movieDetails['runtime']=subtext.time.text.strip()
    movieDetails['release_date']=subtext.find('a',{'title':'See more release dates'})
    
    movieDetails=bs.find('div',{'class':'plot-text'}).div.div.text

    creditSummary=bs.findAll('div',{'class':'credit_summary_item'})

    movieDetails['directors']=[i.text for i in creditSummary[0].findAll('a')]

    movieDetails['writers']=[i.text for i in creditSummary[1].findAll() if 'name' in i.attrs['href'] ]

    movieDetails['cast']=[i.text for i in creditSummary[2].findAll() if 'name' in i.attrs['href']]










if __name__ == "__main__":
    movieName=input('Enter the movie name whose details are to be fetched')
    movieDetails=getMovieDetails(movieName)
★