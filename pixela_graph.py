import requests
from datetime import datetime

USERNAME = # Your Username
TOKEN = # Your Token
GRAPH_ID = # Your Graph ID

profile_page = # Your Page

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

pixela_graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id': 'graph1',
    'name': 'Woodworking Graph',
    'unit': 'commit',
    'type': 'int',
    'color': 'kuro',
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=pixela_graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

graph_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

today = datetime.now()

pixel_config = {
    'date': today.strftime("%Y%m%d"),
    'quantity': input('How many projects did you work on today? '),
}

response = requests.post(url=graph_pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

update_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20231202'

update_pixel_config = {
    'quantity': '0',
}

# response = requests.post(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
# print(response.text)
# 
# response = requests.delete(url=update_pixel_endpoint, headers=headers)
# print(response.text)
