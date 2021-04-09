import requests
import random
from bs4 import BeautifulSoup as bs
from services.categories import get_categories_parsed

def get_random_movie(genres, start_year = 1888, end_year = 2024):
  max_page = 1000
  genres = get_categories_parsed(genres)
  rand_page_num = random.randint(1,max_page)
  url = f'https://www.filmweb.pl/films/search?genres={genres}&orderBy=popularity&descending=true&startYear={start_year}&endYear={end_year}&page={rand_page_num}'
  print(url)
  res = requests.get(url)
  

  i = 2
  while(res.status_code == 404):
    rand_page_num = random.randint(1, max_page/i)
    res = requests.get(url),
    i += 2

  soup = bs(res.content, features="lxml")

  movies = soup.select('.hits__item')
  movie = random.choice(movies)

  card = movie.select('.filmPreview__card')[0]
  poster = 'no poster'
  try:
    poster = movie.select('.filmPreview__poster')[0].select('.poster')[0]['data-image']
  except:
    pass

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