import requests
from datetime import datetime

MY_LAT = 42.361145
MY_LONG = -71.057083
up_lat = MY_LAT + 5
low_lat = MY_LAT - 5
up_long = MY_LONG + 5
low_long = MY_LONG - 5

response = requests.get(url='http://api.open-notify.org/iss-now.json')
response.raise_for_status()

data = response.json()

iss_longitude = float(data['iss_position']['longitude'])
iss_latitude = float(data['iss_position']['latitude'])

iss_position = (iss_latitude, iss_longitude)

# create function that returns true if:
# your position is within +5 or -5 degrees of the ISS position


def check_location():
    if low_lat < iss_latitude < up_lat and low_long < iss_longitude < up_long:
        return True
    else:
        return False


parameters = {
    'lat': MY_LAT,
    'long': MY_LONG,
    'formatted': 0
}

response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data['results']['sunrise'].split('T')[1].split(":")[0])
sunset = int(data['results']['sunset'].split('T')[1].split(":")[0])

time_now = datetime.now()
current_hour = time_now.hour


def check_light():
    if sunset < current_hour < sunrise:
        return True
    else:
        return False

# if the ISS is close to my current position
# and it is currently dark
# then send me an email to tell me to look up
# BONUS: run the code every 60 seconds


check_location()
check_light()
