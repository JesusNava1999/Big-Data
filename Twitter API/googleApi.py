import requests
URL = 'https://maps.googleapis.com/maps/api/js?key=<API_KEY>&libraries=places&callback=initPlaces'
resp = requests.get(URL)

data = resp.json()
#print(data)
#print(data['routes'][0]['legs'][0]['duration']['text'])