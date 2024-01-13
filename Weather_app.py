import requests
import json
import os

city = input("Enter the name of the city\n")

url = f"http://api.weatherapi.com/v1/current.json?key=c9749501d5c94a48b0623417241301&q={city}"

r = requests.get(url)

weather_dic = json.loads(r.text)
w = weather_dic["current"]["temp_c"]

os.system(f"say 'The current weather in {city} is {w} degrees celcius!'")