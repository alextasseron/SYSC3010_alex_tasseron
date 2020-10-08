import http.client
import urllib.parse
import time

key = "AT68QYQ94MQEWXL3"

def personal_info():
    while True:
        group = "L3-T-7"
        cmail = "alextasseron@cmail.carleton.ca"
        member_id = "b"
        
        params = urllib.parse.urlencode({'field1': group, 'field2': cmail, 'field3': member_id, 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print(temp)
            print(response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print("connection failed")
        break
if _name_ == "_main_":
        while True:
                personal_info()