import requests
url = 'https://api.sunrise-sunset.org/json?lat=17.360589&lng=78.4740613&formatted=24'
method = 'GET'
response = requests.request(method, url)
data = response.json()
print( "sunrise of Tehran :",f"{data['results']['sunrise']}")
print( "sunset of Tehran :",f"{data['results']['sunset']}")
"""
برای بدست اوردن طول و عرض جغرافیایی میشود از کد زیر استفاده کرد
# Import the required library
from geopy.geocoders import Nominatim

# Initialize Nominatim API
geolocator = Nominatim(user_agent="MyApp")

location = geolocator.geocode("Hyderabad")

print("The latitude of the location is: ", location.latitude)
print("The longitude of the location is: ", location.longitude)
"""