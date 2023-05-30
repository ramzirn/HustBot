import random
from bs4 import BeautifulSoup
import requests


def rgif():
    url = "https://www.generatormix.com/random-gif-generator?safe="

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    gif_element = soup.find('div', class_='thumbnail-col-1')

    link = soup.find('img', class_='lazy thumbnail')

    src_content = link['data-src']

    return src_content



def lirefichier(f):
    with open(f"{f}", "r") as fichier:
        contenu = fichier.read()
        return (contenu)
    


def get_choice(text):
    sa = text.split(':', 1)[1].strip()
    tableau = sa.split('/')

    tableau_phrases = [phrase.strip() for phrase in tableau]

    return random.choice(tableau_phrases)