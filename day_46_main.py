import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import os
import pprint
import sys

# os.environ['SPOTIPY_CLIENT_ID']
# os.environ['SPOTIPY_CLIENT_SECRET']
# SPOTIPY_REDIRECT_URI = 'http://example.com'

# if len(sys.argv) > 1:
#     search_str = sys.argv[1]
# else:
#     search_str = 'Radiohead'
# 
# sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
# result = sp.search(search_str)
# pprint.pprint(result)

# --------------------------------------- Fetching Top 100 Billboard Info ----------------------------------------

date = input('Which year do want to travel to? Type the date in this format YYYY-MM-DD: \n')

URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(URL)
billboard_webpage = response.text
soup = BeautifulSoup(billboard_webpage, 'html.parser')

groups = soup.find_all('span', class_="a-no-trucate")
music = soup.find_all('h3', class_="a-no-trucate")

artists = [member.getText().strip() for member in groups]
songs = [song.getText().strip() for song in music]

artist_music = [artists[n] + ' - ' + songs[n] for n in range(100)]
print(artist_music)
