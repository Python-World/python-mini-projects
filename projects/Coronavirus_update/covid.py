import json
import urllib.request

country = input("Enter country : ")
url_covid = 'https://coronavirus-19-api.herokuapp.com/countries/' + country
response_covid = urllib.request.urlopen(url_covid)
data_covid = json.loads(response_covid.read())

print("Total Cases :",data_covid['cases'])
print("today Cases :",data_covid['todayCases'])
print("deaths :",data_covid['deaths'])
print("today Deaths :",data_covid['todayDeaths'])
print("recovered :",data_covid['recovered'])
