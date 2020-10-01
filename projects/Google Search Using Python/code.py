from googlesearch import search

query = input()

for item in search(query, tld = "co.in", num=10, stop = 10, pause = 2):
  print(item)