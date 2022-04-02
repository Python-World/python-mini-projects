import sys
from bs4 import BeautifulSoup
from numpy import full
import requests
from colorama import Fore

keyword = sys.argv[1:]

if keyword == []:
    keyword = input("Please enter a keyword: ")
else:
    keyword = "_".join(keyword)

print("Searching for:", keyword + "\n")

req = requests.get("https://en.wikipedia.org/api/rest_v1/page/html/" + keyword)

wiki = BeautifulSoup(req.text, "html.parser").find_all("p")
link = BeautifulSoup(req.text, "html.parser").find("a")["href"]
full_text = []

# get the first 10 paragraphs
for i, p in enumerate(wiki):
    if i == 10:
        break

    if p.text == "":
        continue

    full_text.append(p.text + "\n")

# if there is no text, alert the user about insufficient data
if len(full_text) < 2:
    print(Fore.YELLOW + "No info found for this keyword.\n")
    exit()

# highlight the first paragraph
full_text[0] = Fore.GREEN + full_text[0] + Fore.RESET

# add link to the end of the text
full_text[-1] = (
    "for more information please visit: "
    + Fore.CYAN
    + "https://en.wikipedia.org/wiki/"
    + link[2:]
    + Fore.RESET
)

print("\n".join(full_text))


