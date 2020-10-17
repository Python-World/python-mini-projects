import exifread
import requests
from geopy.geocoders import Nominatim

def format_lati_long(data):
	list_tmp=str(data).replace('[', '').replace(']', '').split(',')
	list=[ele.strip() for ele in list_tmp]
	if (list[-1].find('/') != -1):
		data_sec = int(list[-1].split('/')[0]) /(int(list[-1].split('/')[1])*3600)
	else:
		data_sec = int(list[-1])/3600
	data_minute = int(list[1])/60
	data_degree = int(list[0])
	result=data_degree + data_minute + data_sec
	return result

def get_location(filename):
    img=exifread.process_file(open(filename,'rb'))
    latitude=format_lati_long(str(img['GPS GPSLatitude']))
    longitude=format_lati_long(str(img['GPS GPSLongitude']))
    geolocator = Nominatim(user_agent = "your email")
    position = geolocator.reverse(str(latitude) + ',' + str(longitude))
    return position.address