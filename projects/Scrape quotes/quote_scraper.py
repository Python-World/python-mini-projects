from bs4 import BeautifulSoup
import requests
import csv

# URL to the website
url='http://quotes.toscrape.com'

# Getting the html file and parsing with html.parser
html=requests.get(url)
bs=BeautifulSoup(html.text,'html.parser')

# Tries to open the file 
try:
    csv_file=open('quote_list.csv','w')
    fieldnames=['quote','author','tags']
    dictwriter=csv.DictWriter(csv_file,fieldnames=fieldnames)

    # Writes the headers
    dictwriter.writeheader()

    #While next button is found in the page the loop runs
    while True:
        # Loops through quote in the page
        for quote in bs.findAll('div',{'class':'quote'}):
            #Extract the text part of quote, author and tags
            text=quote.find('span',{'class':'text'}).text
            author=quote.find('small',{'class':'author'}).text
            tags=[]
            for tag in quote.findAll('a',{'class':'tag'}):
                tags.append(tag.text)
            #Writes the current quote,author and tags to a csv file
            dictwriter.writerow({'quote':text,'author':author,'tags':tags})
        
        #Finds the link to next page
        next=bs.find('li',{'class':'next'})
        if not next: 
            break

        #Gets and parses the html file of next page
        html=requests.get(url+next.a.attrs['href'])
        bs=BeautifulSoup(html.text,'html.parser')
except:
    print('Unknown Error!!!')
finally:
    csv_file.close()



    
