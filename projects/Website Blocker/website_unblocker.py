import time
from datetime import datetime as dt

#hostsPath="hosts"
hostsPath=r"C:\Windows\System32\drivers\etc\hosts"

websites=["https://www.sislovesme.com/","https://motherless.com/","https://xhamster.com/","https://www.xnxx.com/","https://www.xvideos.com/","https://www.pornhub.com/"]

with open(hostsPath,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in websites):
                    file.write(line)
            file.truncate()
            