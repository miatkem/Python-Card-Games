import random

class Hand(object):
    def __init__(self):
        self.cards=[]
    
    def add(self, card):
        self.cards.append(card)
        
    def shuffle(self):
        newHand = []
        handSize = len(self.cards)
        for i in range(0,handSize):
            ind = random.randint(0,len(self.cards)-1)
            newHand.append(self.cards.pop(ind))
            
        self.cards=newHand    
    
    def pop(self, index=0):
        return self.cards.pop(index)
    
    def printHand(self):
        print("A hand:" + str(len(self.cards)))
        for card in self.cards:
            card.printCard()