import json
import requests
url = "https://mars.nasa.gov/rss/api/?feed=weather&category=mars2020&feedtype=json"
data = requests.get(url).json()
print("On",data['sols'][6]['terrestrial_date'],"the minimum temperature was ",data['sols'][6]['min_temp'],"on Mars!")