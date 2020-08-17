import requests

# Base Url for geocoding
url = "https://us1.locationiq.com/v1/search.php"

address = input("Input the address: ")

#Your unique private_token should replace value of the private_token variable.
#To know how to obtain a unique private_token please refer the README file for this script.
private_token = "Your_private_token"

data = {
    'key': private_token,
    'q': address,
    'format': 'json'
}

response = requests.get(url, params=data)

latitude = response.json()[0]['lat']
longitude = response.json()[0]['lon']

print(f"The latitude of the given address is: {latitude}")
print(f"The longitude of the given address is: {longitude}")
print("Thanks for using this script")
