import requests
import random
from bs4 import BeautifulSoup as bs

def get_random_movie(genres, start_year = 1950, end_year = 2024):
  url = f'https://www.imdb.com/search/title/?genres={genres}&title_type=feature&explore=genres&year={start_year},{end_year}'
  prep_res = requests.get(url)
  prep_soup = bs(prep_res.content, features="lxml")

  results = prep_soup.select('.desc')[0].select('span')[0].get_text()
  num_of_results = int(results.split(' ')[2].replace(',', ''))
  if num_of_results > 10000: num_of_results = 10000

  page = random.randint(1, num_of_results - 51)
  movie_res = requests.get(url)
  movie_soup = bs(movie_res.content, features="lxml")

  movie = random.choice(movie_soup.select('.lister-item'))
  poster_url = movie.select('img')[0]['src']
  movie_header = movie.select('.lister-item-header')[0]
  title_item = movie_header.select('a')[0]
  imdb_url = title_item['href']
  title = title_item.get_text()
  year = movie_header.select('span')[1].get_text()
  title_year = f'{title} {year}'

  return {
    'title': title_year,
    'poster_url': poster_url,
    'imdb_url': f'https://www.imdb.com{imdb_url}'
  }

  


get_random_movie('comedy', 2017, 2019)