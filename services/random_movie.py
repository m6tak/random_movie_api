import requests
import random
from bs4 import BeautifulSoup as bs
from services.categories import get_categories_parsed

def get_random_movie(genres):
  max_page = 1000
  genres = get_categories_parsed(genres)
  rand_page_num = random.randint(1,max_page)
  res = requests.get(f'https://www.filmweb.pl/films/search?genres={genres}&orderBy=popularity&descending=true&page={rand_page_num}')
  print(f'https://www.filmweb.pl/films/search?genres={genres}&orderBy=popularity&descending=true&page={rand_page_num}')

  i = 2
  while(res.status_code == 404):
    rand_page_num = random.randint(1, max_page/i)
    res = requests.get(f'https://www.filmweb.pl/films/search?genres={genres}&orderBy=popularity&descending=true&page={rand_page_num}'),
    i += 2

  soup = bs(res.content, features="lxml")

  movies = soup.select('.hits__item')
  movie = random.choice(movies)

  card = movie.select('.filmPreview__card')[0]
  poster = movie.select('.filmPreview__poster')[0].select('.poster')[0]['data-image']

  movie_url = card.select('.filmPreview__link')[0]['href']
  filmweb_page = f'https://filmweb.pl{movie_url}'

  title = card.select('.filmPreview__title')[0].get_text()
  year = card.select('.filmPreview__year')[0].get_text()

  return {
    'filmweb_page': filmweb_page,
    'title': title,
    'year': year,
    'poster_url': poster
  }