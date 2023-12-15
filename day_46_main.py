import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import os
import pprint
import sys

# --------------------------------------- Fetching Top 100 Billboard Info ----------------------------------------

# date = input('Which year do want to travel to? Type the date in this format YYYY-MM-DD: \n')
#
# URL = f"https://www.billboard.com/charts/hot-100/{date}"

URL = f"https://www.billboard.com/charts/hot-100/1989-03-31"

response = requests.get(URL)
billboard_webpage = response.text
soup = BeautifulSoup(billboard_webpage, 'html.parser')

groups = soup.find_all('span', class_="a-no-trucate")
music = soup.find_all('h3', class_="a-no-trucate")

artists = [member.getText().strip() for member in groups]
songs = [song.getText().strip() for song in music]

artist_music = [artists[n] + ' - ' + songs[n] for n in range(100)]
print(artist_music)

# -------------------------------------------- Fetching Artist Info ---------------------------------------------

SPOTIPY_REDIRECT_URI = 'http://example.com'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ['SPOTIPY_CLIENT_ID'],
                                               client_secret=os.environ['SPOTIPY_CLIENT_SECRET'],
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope='user-library-read'))

# user_id = sp.current_user()['id']
#
# sp.user_playlist_create(user=user_id,
#                         name=f"{date} Billboard Top 100",
#                         public=False,
#                         collaborative=False,
#                         description=f"Top 100 Songs on {date}")
#
# track_ids = []

# for artist in artists:
#     artist_info = sp.search(artist)
#     pprint.pprint(artist_info['tracks']['items'][0]['artists'][0]['uri'].split(':')[2])

song_info = sp.search('The Bangles - Eternal Flame')

song_uri = song_info['tracks']['items'][0]['uri'].split(':')[2]

# sp.playlist_add_items()
