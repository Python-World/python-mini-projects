import re
import json
import requests
import datetime
from tqdm import tqdm
from bs4 import BeautifulSoup
from collections import defaultdict

submission = defaultdict(list)
#main url
src_url = 'https://www.moneycontrol.com/news/technical-call-221.html'

#get next page links and call scrap() on each link
def setup(url):
    nextlinks = []
    src_page = requests.get(url).text
    src = BeautifulSoup(src_page, 'lxml')

    #ignore <a> with void js as href
    anchors = src.find("div", attrs={"class": "pagenation"}).findAll(
        'a', {'href': re.compile('^((?!void).)*$')})
    nextlinks = [i.attrs['href'] for i in anchors]
    for idx, link in enumerate(tqdm(nextlinks)):
        scrap('https://www.moneycontrol.com'+link, idx)

#scraps passed page url 
def scrap(url, idx):
    src_page = requests.get(url).text
    src = BeautifulSoup(src_page, 'lxml')

    span = src.find("ul", {"id": "cagetory"}).findAll('span')
    img = src.find("ul", {"id": "cagetory"}).findAll('img')

    #<img> has alt text attr set as heading of news, therefore get img link and heading from same tag
    imgs = [i.attrs['src'] for i in img]
    titles = [i.attrs['alt'] for i in img]
    date = [i.get_text() for i in span]

    #list of dicts as values and indexed by page number
    submission[str(idx)].append({'title': titles})
    submission[str(idx)].append({'date': date})
    submission[str(idx)].append({'img_src': imgs})

#save data as json named by current date
def json_dump(data):
    date = datetime.date.today().strftime("%B %d, %Y")
    with open('moneycontrol_'+str(date)+'.json', 'w') as outfile:
        json.dump(submission, outfile)

setup(src_url)
json_dump(submission)

