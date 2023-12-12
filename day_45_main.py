import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.find_all('h3', class_='title')

movies = []

for title in titles:
    movies.insert(0, title.getText())
    with open('movies.txt', 'w') as movie_list:
        for movie in movies:
            movie_list.write(movie + '\n')
