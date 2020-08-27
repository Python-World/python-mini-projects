import requests
from bs4 import BeautifulSoup
#if__name__ == "__main__":

url = input('enter the url: ')

def get(url):
    links =[]
    web = requests.get(url)
    web_Text = web.text
    soup = BeautifulSoup(web_Text, features="html.parser")
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    for link in links:
        print(link)

    #print(len(links))
    print("The number of links in ", url, "is",len(links))

#get("http://fb.com")
get(url)
