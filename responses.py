import random
import random
import requests
from bs4 import BeautifulSoup
from functions.anime import animegen
from functions.film import filmgen,filmgenre
from functions.other import get_choice,lirefichier,rgif




   


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == '!randoma':
        return animegen()
    elif p_message=='!randomf':
        return filmgen()
    elif p_message.startswith("!film"):
        return filmgenre(p_message.split("!film", 1)[1].strip())
    elif p_message =='!listgenre':
        return '`Action/Adventure/Animation/Biography/Comedy/Crime/Drama \nFamily/Fantasy/Film-Noir/History/Horror/Music/Musical/Mystery \nRomance/Sci-Fi/Sport/Thriller/War/Western`'
    
    elif p_message.startswith('!chadimadi:'):
        return get_choice(p_message)
    
    elif p_message=='!gif':
        return rgif()
  
    
    if p_message == '!help':
        return lirefichier("functions/!help.txt")
    


""" def get_response(message: str) -> str:
    p_message = message.lower()

    response_mapping= {
        '!randoma': animegen(),
        '!randomf': filmgen(),
        #'!film': filmgenre(p_message.split("!film", 1)[1].strip()),
        '!listgenre': '`Action/Adventure/Animation/Biography/Comedy/Crime/Drama \nFamily/Fantasy/Film-Noir/History/Horror/Music/Musical/Mystery \nRomance/Sci-Fi/Sport/Thriller/War/Western`',
        '!chadimadi:': get_choice(p_message),
        '!gif': rgif(),
        '!help': lirefichier("functions/!help.txt")
    }
            
    return (response_mapping.get[p_message,'invalid']) """
