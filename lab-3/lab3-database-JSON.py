from urllib.request import * 
from urllib.parse import * 
import json
import sqlite3

# The URL that is formatted: http://api.openweathermap.org/data/2.5/weather?APPID=a808bbf30202728efca23e099a4eecc7&units=imperial&q=ottawa


# As of October 2015, you need an API key.
# I have registered under my Carleton email.
apiKey = "a808bbf30202728efca23e099a4eecc7"

# Query the user for a city
city = input("Enter the name of a city whose weather you want: ")

# Build the URL parameters
params = {"q":city, "units":"imperial", "APPID":apiKey }
arguments = urlencode(params)

# Get the weather information
address = "http://api.openweathermap.org/data/2.5/weather"
url = address + "?" + arguments

print (url)
webData = urlopen(url)
results = webData.read().decode('utf-8')
  # results is a JSON string
webData.close()

print (results)
#Convert the json result to a dictionary
# See http://openweathermap.org/current#current_JSON for the API

data = json.loads(results)

# Print the results

current = data["main"]
degreeSym = chr(176)

print ("Temperature: %d%sF" % (current["temp"], degreeSym ))
print ("Humidity: %d%%" % current["humidity"])
print ("Pressure: %d" % current["pressure"] )

current = data["wind"]

test = ("Wind : %d" % current["speed"])

print(test)

#MY CODE STARTS HERE

connection = sqlite3.connect('lab3JSON.db')

c = connection.cursor()

#c.execute('''CREATE TABLE weather(city TEXT, windspeed TEXT)''')
#forgot to have windspeed as an integer, if the table were created that way I would remove the ' ' around the %s to put it in the table. 

c.execute("INSERT INTO weather (city, windspeed) VALUES ('%s','%s')" % (city, current["speed"]))

connection.commit()

for row in c.execute('SELECT * FROM weather ORDER BY windspeed'):
    print(row)
    
connection.close()





