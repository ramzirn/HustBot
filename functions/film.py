import random
from bs4 import BeautifulSoup
import requests


def filmgen()->str:
    url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

    response = requests.get(url)

    html_content = response.text  
    soup = BeautifulSoup(html_content, 'html.parser')
    anime_elements = soup.select('td.titleColumn')
    
    random_film_element = random.choice(anime_elements)

# Extraire le titre du film
    title = random_film_element.a.text

# Extraire l'année de sortie du film
    year = random_film_element.span.text.strip('()')
    t='Titre :'+title+' '+ '\nAnnee de sortie:'+year
    #print("film aleatoire",random_film)
    return t


def filmgenre(str)->str:
    url = "https://www.imdb.com/search/title/?genres=&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=94365f40-17a1-4450-9ea8-01159990ef7f&pf_rd_r=9B9XC3ZXDSMAC707T072&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_2"

# Trouver la position de "genres="
    index = url.find("genres=")
    
    if index != -1:
       # Insérer "action" juste après "genres="
        url = url[:index + 7] + str + url[index + 7:]
    
    response = requests.get(url)
    i=0
    soup = BeautifulSoup(response.content, "html.parser")

    # Trouver tous les éléments <h3> avec la classe CSS "lister-item-header"
    title_elements = soup.find_all("h3", class_="lister-item-header")

    # Créer une liste pour stocker les titres des films
    titres_films = []

    for title_element in title_elements:
        # Extraire le titre du film en recherchant l'élément <a> et en accédant à son contenu
        titre = title_element.find("a").text.strip()
        titres_films.append(titre)

    # Afficher les titres des films
    for titre in titres_films:
        print(titre)
        #print(i)
        #i=i+1 
    
    
    random_film_element = random.choice(titres_films)
    return random_film_element