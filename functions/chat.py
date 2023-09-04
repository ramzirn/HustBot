import Brainshop
brain = Brainshop.Brain(key="RVJbqTbDU4sVWBop" , bid = 177649)



def getanswer(message ):
    print(brain.ask(message))

message='hello' 
while(message != ' '):
    message=input('-')
    getanswer(message)