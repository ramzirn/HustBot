import Brainshop


# Ouvrir le fichier en mode lecture
with open('token2.txt', 'r') as fichier:
    # Lire la première ligne et la stocker dans une variable
    k = fichier.readline().strip()

    # Lire la deuxième ligne et la stocker dans une autre variable
    id = fichier.readline().strip()



brain = Brainshop.Brain(key=k , bid = id)



def getanswer(message ):
    return (brain.ask(message))

message='hello' 



def supprimer_premier_mot(phrase):
    # Divisez la phrase en mots en utilisant l'espace comme séparateur
    mots = phrase.split()

    # Vérifiez s'il y a au moins un mot dans la phrase
    if len(mots) > 1:
        # Supprimez le premier mot en utilisant un tranchage (slicing)
        phrase_sans_premier_mot = ' '.join(mots[1:])
        return phrase_sans_premier_mot
    else:
        # Si la phrase ne contient qu'un seul mot ou est vide, retournez une chaîne vide
        return ""
