
from bs4 import BeautifulSoup
import requests


url = 'https://yourcountdown.to/everything?search=&tags=Movies&tag_match_type=any&confirmed_status=any&order=most_popular'

response = requests.get(url)

html_content = response.text  
soup = BeautifulSoup(html_content, 'html.parser')
#anime_elements = soup.find_all('div', class_='content')
anime_elements = soup.find_all('div', class_='countdown list is-countdown')
print(anime_elements)

anime_names = [anime.text for anime in anime_elements]


