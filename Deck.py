from Card import Card
from Hand import Hand
import random

class Deck(object):
    def __init__(self):
        self.cards=[]
        self.loadDeck()
    
    def shuffle(self):
        newDeck = []
        deckSize = len(self.cards)
        for i in range(0,deckSize):
            ind = random.randint(0,len(self.cards)-1)
            newDeck.append(self.cards.pop(ind))
        
        self.cards=newDeck
    
    def loadDeck(self):
        suits=["D","H","C","S"]
        faces=["J","Q","K","A"]
        
        for suit in suits:
            for num in range(2,11):
                self.cards.append(Card(str(num), suit))
            for face in faces:
                self.cards.append(Card(face, suit))
    
    def dealHands(self, amtHands, amtCards=0):
        
        if amtHands*amtCards > len(self.cards):
            print("not enough cards in deck to deal")
            return None
        
        #create hands
        hands = []
        for i in range(0,amtHands):
            hands.append(Hand())
            
        #deal certain amount of cards
        if amtCards > 0:
            for i in range(0,amtHands):
                for j in range(0, amtCards):
                    hands[i].add(self.takeTop())
                    
        #deal all cards         
        elif amtCards == 0:
            deckSize = len(self.cards)
            for i in range(0,deckSize):
                hand = i%int(amtHands)
                hands[hand].add(self.takeTop())
        
        else:
            print("invalid amount of card in hands (negative)")
                    
        return hands
        
    def takeTop(self):
        return self.cards.pop()
    
    def printDeck(self):
        for card in self.cards:
            card.printCard()