import requests
url = 'https://api.sunrise-sunset.org/json?lat=17.360589&lng=78.4740613&formatted=24'
method = 'GET'
response = requests.request(method, url)
data = response.json()
print( "sunrise of Tehran :",f"{data['results']['sunrise']}")
print( "sunset of Tehran :",f"{data['results']['sunset']}")