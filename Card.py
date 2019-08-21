from PIL import Image

class Card(object):
    def __init__(self, value, suit, backColor="red"):
        self.value=value
        self.suit=suit
        if suit == "H" or suit == "D":
            self.isRed=True
        else:
            self.isRed=False
        #load image
        path = "images/cards/" + str(suit) + "/" + str(value) + ".png"
        self.frontImg = Image.open(path)
        self.frontImg.load()
        path = "images/cards/back/" + str(backColor) + ".png"
        self.backImg = Image.open(path)
        self.backImg.load()
    
    def printCard(self):
        print(self.value + " of " + self.suit)
        
        