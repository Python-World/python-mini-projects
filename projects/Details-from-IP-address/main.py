from requests import get

def getDetails(ip):
	# source = 'http://ipinfo.io/{}/json'.format(ip)
	source = 'https://ipinfo.io/json'
	response = get(source)
	data = response.json()
	ip = data['ip']
	city = data['city']
	region = data['region']
	country = data['country']
	org = data['org']
	postal = data['postal']
	return "\nIP : {}\nLocation : {}, {}, {}, {}\nISP : {}".format(ip,postal,city,region,country,org)

# test
# print(getDetails("36.31.223.24"))