import requests
import smtplib

# ------------------- Data/Starting Information ------------------------

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
api_key = # ADD Api Key

parameters = {
    'lat': 42.360081,
    'lon': -71.058884,
    'appid': api_key,
    'cnt': 4,
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

weather_alert = ''

# Sender Contact Information
my_email = 'chungus3535@gmail.com'  # Change to real email
password = 'abcd1357)('  # Change to real password

receipt_email = 'bungus5353@gmail.com'  # Change to real email


def get_weather():
    global weather_alert
    for weather_check in weather_data['list']:
        if int(weather_check['weather'][0]['id']) <= 700:
            weather_alert = 'Bring an umbrella!'

            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=receipt_email, msg=weather_alert)

            print(weather_alert)

            return


get_weather()
