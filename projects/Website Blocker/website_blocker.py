import time
from datetime import datetime as dt

#hostsPath="hosts"
hostsPath=r"C:\Windows\System32\drivers\etc\hosts"

redirect="127.0.0.1"
websites=["https://www.sislovesme.com/","https://motherless.com/","https://xhamster.com/","https://www.xnxx.com/","https://www.xvideos.com/","https://www.pornhub.com/"]

with open(hostsPath,'r+') as file:
    content=file.read()
    for site in websites:
        if site in content:
            pass
        else:
            file.write(redirect+" "+site+"\n")
            