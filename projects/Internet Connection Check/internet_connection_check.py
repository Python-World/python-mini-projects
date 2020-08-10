import requests

def internet_connection_test():
	url = 'https://www.google.com/'
	print(f'Attempting to connect to {url} to determine internet connection status.')
	
	try:
		requests.get(url, timeout = 10)
		print(f'Connection to {url} was successful.')
		return True
	except:
		requests.ConnectionError
		print(f'Failed to connect to {url}.')
		return False
	
internet_connection_test()
