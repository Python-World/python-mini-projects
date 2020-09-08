from urllib.request import urlopen
import time

#Storing user defined URl
URL = input("Enter the url whose loading time you want to check: ")

#Open the url as entered by the user and checking protocols
if ("https" or "http") in URL:
    open_this_url = urlopen(URL)

else:
    open_this_url = urlopen("https://" + URL)

#Time stamp before the reading of url starts
start_time = time.time()

#Reading the user defined url
read_the_url = open_this_url.read()

#Time stamp after the reading of the url 
end_time = time.time()

#Closing the instance of the urlopen object
open_this_url.close()

print(f"\nThe time taken to load {URL} is {end_time - start_time} seconds.")
