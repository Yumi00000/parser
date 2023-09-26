from time import sleep

import pandas as pd
import requests
from bs4 import BeautifulSoup

data = []

for num_page in range(1, 31):
    url = f"https://filmix.ac/films/pages/{num_page}"
    print(num_page)
    r = requests.get(url)
    sleep(3)

    soup = BeautifulSoup(r.text, 'lxml')

    films = soup.findAll('article', class_='shortstory line')
    for film in films:
        link = film.find('a', class_='btn-tooltip').get('href')
        title = film.find('h2', class_='name').get('content')
        origin_name = film.find('div', class_='origin-name').get('content')
        genre = film.find('a', itemprop='genre').text
        year = film.find('a', itemprop='copyrightYear').text
        rating = int(film.find('span', class_='rateinf ratePos').text) + int(
            film.find('span', class_='rateinf rateNeg').text)

        data.append([link, title, origin_name, genre, year, rating])

header = ['link', 'title', 'origin_name', 'genre', 'year', 'rating']
df = pd.DataFrame(data, columns=header)
df.to_csv('parserHTML.csv', sep=';', encoding='utf8')


print('\n'.join(map(str, data)))
