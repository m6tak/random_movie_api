import requests
import random
from bs4 import BeautifulSoup as bs

rand_page_num = random.randint(1,500)
rand_page = requests.get(f'https://www.filmweb.pl/films/search?orderBy=popularity&descending=true&page={rand_page_num}').content
soup = bs(rand_page, features="lxml")

titles = soup.find_all(class_='filmPreview__title')
titles_text = [title.get_text() for title in titles]

print(random.choice(titles_text))