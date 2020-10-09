import requests
from lxml import html
import re
import sys
import pprint
from profilepic import pp_download

def banner():
    print('\t""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""')
    print('\t                         InstgramProfile data graber                    ')
    print('\t""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""')


def main(username):
    banner()
    '''main function accept instagram username
    return an dictionary object containging profile deatils
    '''

    url = "https://www.instagram.com/{}/?hl=en".format(username)
    page = requests.get(url)
    tree = html.fromstring(page.content)
    data = tree.xpath('//meta[starts-with(@name,"description")]/@content')

    if data:
        data = tree.xpath('//meta[starts-with(@name,"description")]/@content')
        data = data[0].split(', ')
        followers = data[0][:-9].strip()
        following = data[1][:-9].strip()
        posts = re.findall(r'\d+[,]*', data[2])[0]
        name = re.findall(r'name":"([^"]+)"', page.text)[0]
        aboutinfo = re.findall(r'"description":"([^"]+)"', page.text)[0]
        instagram_profile = {
            'success': True,
            'profile': {
                'name': name,
                'profileurl': url,
                'username': username,
                'followers': followers,
                'following': following,
                'posts': posts,
                'aboutinfo': aboutinfo
            }
        }
    else:
        instagram_profile = {
            'success': False,
            'profile': {}
        }
    return instagram_profile


#  python main.py username
if __name__ == "__main__":

    if len(sys.argv) == 2:
        output = main(sys.argv[-1])
        pp_download(sys.argv[-1])
        pprint.pprint(output)
        
    else:
        print('Invalid paramaters Valid Command \n\tUsage : python main.py username')
