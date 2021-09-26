#Program to fetch the http status code give the url/api
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import emoji

#Taking input url from user
requestURL = input("Enter the URL to be invoked: ")

#Gets the response from URL and prints the status code, corresponding emoji and message accordingly
try:
    response = urlopen(requestURL)
    #In case of success, prints success status code and thumbs_up emoji
    print('Status code : ' + str(response.code) + ' ' + emoji.emojize(':thumbs_up:'))
    print('Message : ' + 'Request succeeded. Request returned message - ' + response.reason)
except HTTPError as e:
    #In case of request failure, prints HTTP error status code and thumbs_down emoji
    print('Status : ' + str(e.code) + ' ' + emoji.emojize(':thumbs_down:'))
    print('Message : Request failed. Request returned reason - ' + e.reason)
except URLError as e:
    #In case of bad URL or connection failure, prints Win Error and thumbs_down emoji
    print('Status :',  str(e.reason).split(']')[0].replace('[','') +  ' ' + emoji.emojize(':thumbs_down:'))
    print('Message : '+ str(e.reason).split(']')[1])
