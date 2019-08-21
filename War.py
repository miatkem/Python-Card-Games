from Card import Card
from Deck import Deck
from Hand import Hand

class War(object):
    def __init__(self):
        self.status = "not delt"
        self.deck = Deck()
        self.hands = []
        self.playerUsedPile=Hand()
        self.computerUsedPile=Hand()
        self.warCounter=0
        self.rewardPile=[]
    
    def deal(self):
        self.status = "normal fight"
        self.deck.shuffle()
        self.hands=self.deck.dealHands(2)
        self.playerUsedPile=Hand()
        self.computerUsedPile=Hand()
    
    def flip(self):
        if self.status == "normal fight":
            playerCard = self.hands[0].pop()
            computerCard = self.hands[1].pop()
                    
            if self.getCardValue(playerCard) > self.getCardValue(computerCard):
                self.playerUsedPile.add(playerCard)
                self.playerUsedPile.add(computerCard)
            elif self.getCardValue(playerCard) < self.getCardValue(computerCard):
                self.computerUsedPile.add(playerCard)
                self.computerUsedPile.add(computerCard)
            else:
                self.rewardPile.append(playerCard)
                self.rewardPile.append(computerCard)
                self.status="war"
                self.warCounter=3
            
        elif self.status == "war":
            if self.warCounter > 0:
                self.rewardPile.append(self.hands[0].pop())
                self.rewardPile.append(self.hands[1].pop())
                self.warCounter-=1
            elif self.warCounter == 0:
                
                playerCard = self.hands[0].pop()
                computerCard = self.hands[1].pop()     
                
                if self.getCardValue(playerCard) > self.getCardValue(computerCard):
                    self.playerUsedPile.add(playerCard)
                    self.playerUsedPile.add(computerCard)
                    for card in self.rewardPile:
                        self.playerUsedPile.add(card)
                    self.rewardPile=[]
                    self.status = "normal fight"
                    self.warCounter-=1

                elif self.getCardValue(playerCard) < self.getCardValue(computerCard):
                    self.computerUsedPile.add(playerCard)
                    self.computerUsedPile.add(computerCard)    
                    for card in self.rewardPile:
                        self.computerUsedPile.add(card)
                    self.rewardPile=[]
                    self.status = "normal fight"
                    self.warCounter-=1
                else:
                    self.rewardPile.append(playerCard)
                    self.rewardPile.append(computerCard)
                    self.status="war"
                    self.warCounter=3
        self.checkHandSizes()
            
    def checkHandSizes(self):
        if len(self.hands[0].cards) == 0:
            if len(self.playerUsedPile.cards) == 0:
                self.status = "gameover"
            else:
                self.playerUsedPile.shuffle()
                self.hands[0] = self.playerUsedPile
                self.playerUsedPile = Hand()
            
        if len(self.hands[1].cards) == 0:
            if len(self.computerUsedPile.cards) == 0:
                self.status = "gameover"
            else:
                self.computerUsedPile.shuffle()
                self.hands[1] = self.computerUsedPile
                self.computerUsedPile= Hand()
        
    def getCardValue(self, card):
        if ord(card.value[0]) < 50 or ord(card.value[0]) > 57:
            if ord(card.value[0]) == 49:
                return 10
            elif ord(card.value[0]) == 74:
                return 11
            elif ord(card.value[0]) == 81:
                return 12
            elif ord(card.value[0]) == 75:
                return 13
            elif ord(card.value[0]) == 65:
                return 14
        else:
            return int(card.value)
                
            
        