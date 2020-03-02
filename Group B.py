import random
randomWords = ["ducks", "jumbo", "lucky", "pills", "flour"]
secret = random.choice (randomWords)
letter = ""
updateWord = []
def initialize():
    print "We have a secret word"
    print "_ _ _ _ _"
def getLetter():
    print ("Enter a letter")
    global letter
    letter = raw_input()
def ifWon():
    if secret == updateWord:
        print ("you win")
    else:
        getLetter()
        
def test():
    global updatedWord
    life = 6
    if updatedWord == secret:
        ifWon()
    elif
        lives=life-1
        return lives
        
    else life = 0:
        print=("you lost")         

        
def main():
    initialize ()
    getLetter ()
    ifWon()
main()
    
#def tester():
    #print updateWord
    #updateWord = raw_input()
    #if updateWord== secret:
        #print ("okay")
    #else: 
        #print ("no")
