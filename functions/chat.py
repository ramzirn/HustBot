import Brainshop
brain = Brainshop.Brain(key="RVJbqTbDU4sVWBop" , bid = 177649)



def getanswer(message ):
    print(brain.ask(message))

message='hello' 
while(message != ' '):
    message=input('-')
    getanswer(message)



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
