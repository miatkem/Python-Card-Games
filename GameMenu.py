from tkinter import *
from PIL import Image, ImageTk
from Card import Card
from Deck import Deck
from Hand import Hand
from War import War

def quit():
    exit()

    
def startWar():
    print("wow")
    def gameoverMsg():
        winMessage = Toplevel()
        winMessage.wm_title("GAME OVER")
        if len(war.hands[0].cards) > 0:
            l = Label(winMessage, text="YOU WIN").grid(row=0, column=0)
        else:
            l = Label(winMessage, text="YOU LOSE").grid(row=0, column=0)
        b = Button(winMessage, text="Play Again?", command = lambda:[winMessage.destroy(),startWar()]).grid(row=1, column=0)    
    def flip():
        
        if war.status == "gameover":
            gameoverMsg()
        
        if len(war.hands[0].cards) > 0:
            playerDeckImg=ImageTk.PhotoImage(war.hands[0].cards[0].backImg.resize((100,150)))
        else:
            playerDeckImg=ImageTk.PhotoImage(Image.open("images/cards/blank.png").resize((100,150)))
        playerDeck.configure(image=playerDeckImg)
        playerDeck.image=playerDeckImg 
        if len(war.hands[1].cards) > 0:
            computerDeckImg=ImageTk.PhotoImage(war.hands[1].cards[0].backImg.resize((100,150)))
        else:
            computerDeckImg=ImageTk.PhotoImage(Image.open("images/cards/blank.png").resize((100,150)))        
        computerDeck.configure(image=computerDeckImg)
        computerDeck.image=computerDeckImg 
        if len(war.playerUsedPile.cards) > 0:
            usedPlayerDeckImg=ImageTk.PhotoImage(war.playerUsedPile.cards[0].backImg.resize((100,150)))
        else:
            usedPlayerDeckImg=ImageTk.PhotoImage(Image.open("images/cards/blank.png").resize((100,150)))        
        usedPlayerDeck.configure(image=usedPlayerDeckImg)
        usedPlayerDeck.image=usedPlayerDeckImg 
        if len(war.computerUsedPile.cards) > 0:
            usedComputerDeckImg=ImageTk.PhotoImage(war.computerUsedPile.cards[0].backImg.resize((100,150)))
        else:
            usedComputerDeckImg=ImageTk.PhotoImage(Image.open("images/cards/blank.png").resize((100,150)))        
        usedComputerDeck.configure(image=usedComputerDeckImg)
        usedComputerDeck.image=usedComputerDeckImg         
        
        if war.status == "war":
            if war.warCounter == 3:
                if len(war.hands[0].cards) > 0:
                    playerWarSpotOneImg=ImageTk.PhotoImage(war.hands[0].cards[0].frontImg.resize((100,150)))
                    playerWarSpotOne.configure(image=playerWarSpotOneImg)
                    playerWarSpotOne.image=playerWarSpotOneImg
                if len(war.hands[1].cards) > 0:
                    computerWarSpotOneImg=ImageTk.PhotoImage(war.hands[1].cards[0].frontImg.resize((100,150)))
                    computerWarSpotOne.configure(image=computerWarSpotOneImg)
                    computerWarSpotOne.image=computerWarSpotOneImg                
                
            elif war.warCounter == 2 or war.warCounter == 0:
                if len(war.hands[0].cards) > 0:
                    playerCardImg=ImageTk.PhotoImage(war.hands[0].cards[0].frontImg.resize((100,150)))
                    playerCard.configure(image=playerCardImg)
                    playerCard.image=playerCardImg
                if len(war.hands[1].cards) > 0:
                    computerCardImg=ImageTk.PhotoImage(war.hands[1].cards[0].frontImg.resize((100,150)))
                    computerCard.configure(image=computerCardImg)
                    computerCard.image=computerCardImg                
            
            elif war.warCounter == 1:
                if len(war.hands[0].cards) > 0:
                    playerWarSpotThreeImg=ImageTk.PhotoImage(war.hands[0].cards[0].frontImg.resize((100,150)))
                    playerWarSpotThree.configure(image=playerWarSpotThreeImg)
                    playerWarSpotThree.image=playerWarSpotThreeImg
                if len(war.hands[1].cards) > 0:
                    computerWarSpotThreeImg=ImageTk.PhotoImage(war.hands[1].cards[0].frontImg.resize((100,150)))
                    computerWarSpotThree.configure(image=computerWarSpotThreeImg)
                    computerWarSpotThree.image=computerWarSpotThreeImg
        else:
            playerWarSpotThreeImg=ImageTk.PhotoImage(Image.open("images/cards/blank.png").resize((100,150)))
            playerWarSpotThree.configure(image=playerWarSpotThreeImg)
            playerWarSpotThree.image=playerWarSpotThreeImg
            computerWarSpotThreeImg=ImageTk.PhotoImage(Image.open("images/cards/blank.png").resize((100,150)))
            computerWarSpotThree.configure(image=computerWarSpotThreeImg)
            computerWarSpotThree.image=computerWarSpotThreeImg
            playerWarSpotOneImg=ImageTk.PhotoImage(Image.open("images/cards/blank.png").resize((100,150)))
            playerWarSpotOne.configure(image=playerWarSpotOneImg)
            playerWarSpotOne.image=playerWarSpotOneImg
            computerWarSpotOneImg=ImageTk.PhotoImage(Image.open("images/cards/blank.png").resize((100,150)))
            computerWarSpotOne.configure(image=computerWarSpotOneImg)
            computerWarSpotOne.image=computerWarSpotOneImg            
            
            if len(war.hands[0].cards) > 0:
                playerCardImg=ImageTk.PhotoImage(war.hands[0].cards[0].frontImg.resize((100,150)))
                playerCard.configure(image=playerCardImg)
                playerCard.image=playerCardImg
            if len(war.hands[1].cards) > 0:
                computerCardImg=ImageTk.PhotoImage(war.hands[1].cards[0].frontImg.resize((100,150)))
                computerCard.configure(image=computerCardImg)
                computerCard.image=computerCardImg
            
            playerCardCount = Label(win, text = "Cards: " + str(len(war.hands[0].cards) + len(war.playerUsedPile.cards))).grid(row=5, column=1)
            computerCardCount = Label(win, text =  "Cards: " + str(len(war.hands[1].cards) + len(war.computerUsedPile.cards))).grid(row=1, column=1)
        war.flip()
    
    war = War()
    war.deal()
    
    compDeckLabel = Label(win, text =  "Computer's Cards").grid(row=0, column=0)
    compUsedDeckLabel = Label(win, text =  "Computer's Pile").grid(row=0, column=2)
    
    playerCardCount = Label(win, text =  "Cards: 5").grid(row=3, column=1)
    
    computerDeckImg=ImageTk.PhotoImage(war.hands[1].cards[0].backImg.resize((100,150)))
    computerDeck = Label(win, image=computerDeckImg)
    computerDeck.grid(row=1, column=0)
    computerDeck.image=computerDeckImg
    
    computerCardCount = Label(win, text =  "Cards: " + str(len(war.hands[1].cards))).grid(row=1, column=1)
    
    usedComputerDeckImg=ImageTk.PhotoImage(Image.open("images/cards/blank.png").resize((100,150)))
    usedComputerDeck = Label(win, image=usedComputerDeckImg)
    usedComputerDeck.grid(row=1, column=2)
    usedComputerDeck.image=usedComputerDeckImg
    
    computerWarSpotOneImg = ImageTk.PhotoImage(Image.open("images/cards/blank.png").resize((100,150)))
    computerWarSpotOne = Label(win, image=computerWarSpotOneImg)
    computerWarSpotOne.grid(row=2, column=0)
    computerWarSpotOne.image=computerWarSpotOneImg
    
    computerCardImg = ImageTk.PhotoImage(Image.open("images/cards/blank.png").resize((100,150)))
    computerCard = Label(win, image=computerCardImg)
    computerCard.grid(row=2, column=1)
    computerCard.image=computerCardImg
    
    computerWarSpotThreeImg = ImageTk.PhotoImage(Image.open("images/cards/blank.png").resize((100,150)))
    computerWarSpotThree = Label(win, image=computerWarSpotThreeImg)
    computerWarSpotThree.grid(row=2, column=2)
    computerWarSpotThree.image=computerWarSpotThreeImg
    
    playerWarSpotOneImg = ImageTk.PhotoImage(Image.open("images/cards/blank.png").resize((100,150)))
    playerWarSpotOne = Label(win, image=playerWarSpotOneImg)
    playerWarSpotOne.grid(row=3, column=0)
    playerWarSpotOne.image=playerWarSpotOneImg
    
    playerCardImg = ImageTk.PhotoImage(Image.open("images/cards/blank.png").resize((100,150)))
    playerCard = Label(win, image=playerCardImg)
    playerCard.grid(row=3, column=1)
    playerCard.image=playerCardImg
    
    playerWarSpotThreeImg = ImageTk.PhotoImage(Image.open("images/cards/blank.png").resize((100,150)))
    playerWarSpotThree = Label(win, image=playerWarSpotThreeImg)
    playerWarSpotThree.grid(row=3, column=2)
    playerWarSpotThree.image=playerWarSpotThreeImg    
    
    playerDeckLabel = Label(win, text =  "Your Cards").grid(row=4, column=0)
    playerUsedDeckLabel = Label(win, text =  "Your Pile").grid(row=4, column=2)    
    
    playerDeckImg=ImageTk.PhotoImage(war.hands[0].cards[0].backImg.resize((100,150)))
    playerDeck = Button(win, image=playerDeckImg,command=flip)
    playerDeck.grid(row=5, column=0)
    playerDeck.image=playerDeckImg
    
    playerCardCount = Label(win, text = "Cards: " + str(len(war.hands[0].cards))).grid(row=5, column=1)
    
    usedPlayerDeckImg=ImageTk.PhotoImage(Image.open("images/cards/blank.png").resize((100,150)))
    usedPlayerDeck = Label(win, image=usedPlayerDeckImg)
    usedPlayerDeck.grid(row=5, column=2)
    usedPlayerDeck.image=usedPlayerDeckImg
    
win = Tk()
win.title("Python Card Games")
menuBar = Menu(win)

options = Menu(menuBar, tearoff=0)
options.add_command(label = "Close", command=quit)

games = Menu(menuBar, tearoff=0)
games.add_command(label = "War", command=startWar)


menuBar.add_cascade(label = "Card Games", menu=games)
menuBar.add_cascade(label = "Options", menu=options)


win.config(menu=menuBar)
win.mainloop()