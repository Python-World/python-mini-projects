import requests

def Internet_Connection_Test():
	
    '''This function will attempt to connect to Google to check the status of the internet''' 
    
    
    url = 'https://www.google.com/'
	
	print(f'Attempting to connect to {url} to determine internet connection status.')
	
    try:
		requests.get(url, timeout = 10)
		print(f'Connection to {url} was successful.')
		return True
	except requests.ConnectionError:
		print(f'Failed to connect to {url}.')
		return False

Internet_Connection_Test()
