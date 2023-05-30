import random
from bs4 import BeautifulSoup
import requests


def animegen()->str:
    url = 'https://myanimelist.net/topanime.php?limit='
    url=url+str(getu())
    response = requests.get(url)

    html_content = response.text  
    soup = BeautifulSoup(html_content, 'html.parser')
    anime_elements = soup.find_all('td', class_='title al va-t word-break')

    anime_names = [anime.text for anime in anime_elements]
  
    random_anime = random.choice(anime_names)

    return random_anime



def getu(): 

    list = []

    
    s=10550
    while s >0:
        s=s-50
        list.append(s)
        

    return (random.choice(list))