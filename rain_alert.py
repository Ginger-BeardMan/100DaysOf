import requests

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
api_key = '93f383bb55bd8e5fe23a38938e1475f2'

parameters = {
    'lat': 42.360081,
    'lon': -71.058884,
    'appid': api_key,
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()
