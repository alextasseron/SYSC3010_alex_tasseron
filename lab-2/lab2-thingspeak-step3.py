# READ KEY 9SO0XFLPB59ODN5L
#Credit to Soumilshah1995 for the code

import urllib.request
import requests
import threading
import json

def read_data_thingspeak():
    
    url = 'https://api.thingspeak.com/channels/1160858/fields/1.json?api_key='
    key = '9SO0XFLPB59ODN5L'
    header = '&results=2'
    urlConc = url + key + header
    
    print (urlConc)
    
    get_data = requests.get(urlConc).json()
    
    print (get_data)
    
    channel_id = get_data['channel']['id']
    
    field_1 = get_data['feeds']
    
    t = []
    
    for x in field_1:
        t.append(x['field1'])

if __name__ == '__main__':
    
    read_data_thingspeak()