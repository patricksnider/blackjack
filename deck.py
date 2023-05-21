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
            for val in range(2, 15):
                for suit in ["S", "C", "D", "H"]:
                    self.cards.append(Card(val, suit, x))

    def destroy(self):
        self.cards = []

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

    def dealInitialCardsPlayers(self, players):
        for i in range(2):
            for player in players:
                self.dealCard(player)

    def dealInitialCardsDealer(self, dealer):
        for i in range(2):
            self.dealCard(dealer)
    
class Dealer:
    def __init__(self):
        self.players = []
        self.cards = []
        self.count = [0,0]
        self.bestCount = 0

    def showHalfCards(self):
        print("Dealer's Cards:")
        self.cards[0].show()
        print("2nd Card: ?\n")

    def showCards(self):
        print("Dealers's cards:")
        for card in self.cards:
            card.show()

    def showBestCount(self):
        print("Dealer's Best Count: {}\n".format(self.bestCount))

    def hit(self, deck):
        deck.dealCard(self)
        self.showCards()
        self.showCount()

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
        if(self.count[0] == self.count[1]):
            self.bestCount = self.count[0]
        elif(self.count[1] > 21):
            self.bestCount = self.count[0]
        elif(self.count[1] > self.count[0] and self.count[1] < 22):
            self.bestCount = self.count[1]
        else:
            self.bestCount = self.count[0]

    def showCount(self):
        if(self.count[0] == self.count[1]):
            print("Dealer's Count: {}\n".format(self.count[0]))
        elif(self.count[0] != self.count[1] and (self.count[0] and self.count[1]) < 22):
            print("Dealer's Count: {}/{}\n".format(self.count[0], self.count[1]))
        elif(self.count[0] != self.count[1] and (self.count[0] < 22 and self.count[1] > 21)):
            print("Dealer's Count: {}\n".format(self.count[0]))
        elif(self.count[0] != self.count[1] and (self.count[1] < 22 and self.count[0] > 21)):
            print("Dealer's Count: {}\n".format(self.count[1]))

class Player:
    def __init__(self, money, name):
        self.cards = []
        self.count = [0,0]
        self.bestCount = 0
        self.balance = money
        self.name = name
        self.playerBet = 0

    def showCards(self):
        print("{}'s cards:".format(self.name))
        for card in self.cards:
            card.show()

    def showBal(self):
        print("{}'s Balance: {}".format(self.name, self.balance))

    def showBestCount(self):
        print("{}'s Best Count: {}".format(self.name, self.bestCount))

    def promptBet(self):
        return input("{}, what is your bet?\n".format(self.name))

    def bet(self, val):
        bet = val
        if(bet <= self.balance):
            self.balance = self.balance - bet
            self.playerBet = bet
        else:
            print("Not enough money\n")

    def successfulBet(self):
        print("{} wins {}!!".format(self.name, self.playerBet))
        if(len(self.cards) == 2 and self.count[1] == 21):
            self.balance = self.balance + (self.playerBet*2.5)
            self.playerBet = 0
        else:
            self.balance = self.balance + (self.playerBet*2)
            self.playerBet = 0
    def unsuccessfulBet(self):
        self.playerBet = 0

    def pushBet(self):
        self.balance = self.balance + self.playerBet
        self.playerBet = 0

    def hit(self, deck):
        deck.dealCard(self)
        self.showCards()
        self.showCount()
        
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
        if(self.count[0] == self.count[1]):
            self.bestCount = self.count[0]
        elif(self.count[1] > 21):
            self.bestCount = self.count[0]
        elif(self.count[1] > self.count[0] and self.count[1] < 22):
            self.bestCount = self.count[1]
        else:
            self.bestCount = self.count[0]

    def showCount(self):
        if(self.count[0] > 21 and self.count[1] > 21):
            print("{}'s Count: bust\n".format(self.name))
        elif(self.count[0] == self.count[1]):
            print("{}'s Count: {}\n".format(self.name, self.count[0]))
        elif(self.count[0] != self.count[1] and (self.count[0] and self.count[1]) < 22):
            print("{}'s Count: {}/{}\n".format(self.name, self.count[0], self.count[1]))
        elif(self.count[0] != self.count[1] and (self.count[0] < 22 and self.count[1] > 21)):
            print("{}'s Count: {}\n".format(self.name, self.count[0]))
        elif(self.count[0] != self.count[1] and (self.count[1] < 22 and self.count[0] > 21)):
            print("{}'s Count: {}\n".format(self.name, self.count[1]))

def dealerRound(dealer, deck):
    while(dealer.bestCount < 17):
        dealer.hit(deck)


def playerRound(player, deck):
    direction = input("Enter hit to hit or stand to stand\n")
    if(direction == "hit"):
        player.hit(deck)
        if(player.bestCount < 22):
            playerRound(player, deck)
        else:
            print("Bust!\n")
    elif(direction == "stand"):
        player.showCards()
        player.showCount()
    else:
        print("Enter a correct direction\n")
        playerRound(player, deck)

def compareHands(hand1, hand2):
    if(hand1.bestCount > 21 and hand2.bestCount < 22):
        return -1
    elif(hand2.bestCount > 21 and hand1.bestCount < 22):
        return 1
    elif(hand1.bestCount > hand2.bestCount):
        return 1
    elif(hand1.bestCount < hand2.bestCount):
        return -1
    else:
        return 0

def startRound(deck, players, dealer):
    for player in players:
        betAmt = int(player.promptBet())
        player.bet(betAmt)
    deck.dealInitialCardsPlayers(players)
    deck.dealInitialCardsDealer(dealer)
    dealer.showHalfCards()
    for player in players:
        player.showCards()
        player.showCount()

    for player in players:
        playerRound(player, deck)

    dealerRound(dealer, deck)


    for player in players:
        results = compareHands(dealer, player)
        if(results == -1):
            player.successfulBet()
        elif(results == 1):
            player.unsuccessfulBet()
            print("House Wins!\n")
        else:
            player.pushBet()
            print("Push")

def resetRound(deck, players, dealer):
    deck.destroy()
    deck.create()
    deck.shuffle(2)
    for player in players:
        player.cards = []
        player.count = [0,0]
        player.bestCount = 0
    dealer.cards = []
    dealer.count = [0,0]
    dealer.bestCount = 0

    
def startGame():
    deck = Deck(6)
    dealer = Dealer()
    player1 = Player(100, "Pat")
    players = [player1]
    mes = "start"
    while(mes == "start"):
        mes = input("Enter 'start' to begin next round, 'bal' to check balance\n")
        if(mes == "bal"):
            print(player1.balance)
            mes = "start"
        elif(mes == "start"):
            startRound(deck, players, dealer)
            resetRound(deck, players, dealer)


startGame()