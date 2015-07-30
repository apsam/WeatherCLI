#!/usr/bin/env python3

try:
	from urllib.request import urlopen
except ImportError:
	from urllib2 import urlopen
import json
import sys
import configparser

config = configparser.ConfigParser()
#configFilePath = r'.\keys.txt'
#configParser.read(configFilePath)
#API_KEY = configParser.get('Key Section', 'API')
config.read('keys.txt')
section = config['Key Section']
API_KEY = section['API']
u_city = sys.argv[1]
u_state = sys.argv[2]

site = 'http://api.wunderground.com/api/'+API_KEY+'/conditions/q/'+u_state+'/'+u_city+'.json'

response = urlopen(site)
json_string = response.read().decode('utf-8')

parsed_json = json.loads(json_string)

location = parsed_json['current_observation']['display_location']['city']

temp_f = parsed_json['current_observation']['temp_f']

#print("Current temperature in %s is %s") % (location, temp_f)
print("Current temperature in")
print(location)
print("is")
print(temp_f)

response.close()
