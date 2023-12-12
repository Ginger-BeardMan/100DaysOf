import requests
from bs4 import BeautifulSoup

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
