import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import os

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

# -------------------------------------------- Fetching Artist Info ---------------------------------------------

SPOTIPY_REDIRECT_URI = 'http://example.com'

OAUTH_AUTHORIZE_URL = 'https://accounts.spotify.com/authorize'

OAUTH_TOKEN_URL = 'https://accounts.spotify.com/api/token'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ['SPOTIPY_CLIENT_ID'],
                                               client_secret=os.environ['SPOTIPY_CLIENT_SECRET'],
                                               redirect_uri=SPOTIPY_REDIRECT_URI, state=None,
                                               scope='playlist-modify-private', cache_path=".cache",
                                               username=os.environ['SPOTIFY_USER_NAME'], show_dialog=True))

user_id = sp.current_user()['id']

song_uris = []

playlist = sp.user_playlist_create(user=user_id,
                                   name=f"{date} Billboard Top 100",
                                   public=False, collaborative=False, description=f"Top 100 Songs on {date}")

PLAYLIST_ID = playlist['id']

for artist_song in artist_music:
    try:
        song_info = sp.search(artist_song)
        song_uri = song_info['tracks']['items'][0]['uri'].split(':')[2]

        song_uris.append(song_uri)
    except IndexError:
        print(f"{artist_song} doesn't exist in Spotify. Skipped.")

sp.playlist_add_items(playlist_id=PLAYLIST_ID, items=song_uris, position=None)
