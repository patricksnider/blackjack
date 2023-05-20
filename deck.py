import random
class Card:
    def __init__(self, value, suit, deckNum):
        self.value = value
        self.suit = suit
        self.deckNum = deckNum

    def show(self):
        print("{} of {}".format(self.value, self.suit))

class Deck:
    def __init__(self, deckNum):
        self.cards = []
        #number of decks in the game
        self.deckNum = deckNum
        self.create()
        #shuffles cards twice
        self.shuffle(2)

    def create(self):
        for x in range(1, self.deckNum+1):
            for val in range(1, 14):
                for suit in ["S", "C", "D", "H"]:
                    self.cards.append(Card(val, suit, x))

    def show(self):
        for card in self.cards:
            card.show()
    
    def deckCount(self):
        print("Card Count: {}".format(len(self.cards)))

    def shuffle(self, shuffleNum):
        for num in range(shuffleNum):
            random.shuffle(self.cards)

    def dealCard(self, player):
        player.cards.append(self.cards.pop())
        player.updateCount()

    def dealInitialCards(self, players):
        for i in range(2):
            for player in players:
                self.dealCard(player)

    
class Dealer:
    def __init__(self):
        self.players = []
        self.cards = []
        self.count = [0,0]

    def showCards(self):
        print("Dealers's cards:")
        for card in self.cards:
            card.show()

    def hit(self):
        deck.dealCard(self)
        self.showCards()

    def updateCount(self):
        self.count = [0,0]
        for card in self.cards:
            if(card.value < 11):
                self.count[0] = self.count[0]+card.value
                self.count[1] = self.count[1]+card.value
            elif(card.value < 14):
                self.count[0] = self.count[0]+10
                self.count[1] = self.count[1]+10
            elif(card.value == 14):
                self.count[1] = self.count[0]
                self.count[0] = self.count[0]+1
                self.count[1] = self.count[1]+11

    def showCount(self):
        if(self.count[0] == self.count[1]):
            print("Dealer's Count: {}".format(self.count[0]))
        elif(self.count[0] != self.count[1] and (self.count[0] and self.count[1]) < 22):
            print("Dealer's Count: {}/{}".format(self.count[0], self.count[1]))
        elif(self.count[0] != self.count[1] and (self.count[0] < 22 and self.count[1] > 21)):
            print("Dealer's Count: {}".format(self.count[0]))
        elif(self.count[0] != self.count[1] and (self.count[1] < 22 and self.count[0] > 21)):
            print("Dealer's Count: {}".format(self.count[1]))

class Player:
    def __init__(self, money, name):
        self.cards = []
        self.count = [0,0]
        self.balance = money
        self.name = name
        self.playerBet = 0

    def showCards(self):
        print("{}'s cards:".format(self.name))
        for card in self.cards:
            card.show()

    def showBal(self):
        print("{}'s Balance: {}".format(self.name, self.balance))

    def bet(self, val):
        bet = val
        if(bet < self.balance):
            self.balance = self.balance - bet
            self.playerBet = bet
        else:
            print("Not enough money")

    def hit(self):
        deck.dealCard(self)
        self.showCards()
        
    def updateCount(self):
        self.count = [0,0]
        for card in self.cards:
            if(card.value < 11):
                self.count[0] = self.count[0]+card.value
                self.count[1] = self.count[1]+card.value
            elif(card.value < 14):
                self.count[0] = self.count[0]+10
                self.count[1] = self.count[1]+10
            elif(card.value == 14):
                self.count[1] = self.count[0]
                self.count[0] = self.count[0]+1
                self.count[1] = self.count[1]+11

    def showCount(self):
        if(self.count[0] == self.count[1]):
            print("{}'s Count: {}".format(self.name, self.count[0]))
        elif(self.count[0] != self.count[1] and (self.count[0] and self.count[1]) < 22):
            print("{}'s Count: {}/{}".format(self.name, self.count[0], self.count[1]))
        elif(self.count[0] != self.count[1] and (self.count[0] < 22 and self.count[1] > 21)):
            print("{}'s Count: {}".format(self.name, self.count[0]))
        elif(self.count[0] != self.count[1] and (self.count[1] < 22 and self.count[0] > 21)):
            print("{}'s Count: {}".format(self.name, self.count[1]))
deck = Deck(6)
player1 = Player(100, "Pat")
dealer = Dealer()
players = [player1, dealer]
deck.deckCount()
player1.showBal()
player1.bet(10)
player1.showBal()
player1.bet(91)
deck.dealInitialCards(players)
player1.showCards()
player1.showCount()
dealer.showCards()
dealer.showCount()
deck.deckCount()
player1.hit()
player1.showCount()
deck.deckCount()
dealer.hit()
dealer.showCount()
deck.deckCount()
