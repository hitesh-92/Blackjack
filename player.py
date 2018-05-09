class Player():
    """
    Player Class. Holds bankBalance, amountBet, cards held and value of cards
    """
    def __init__(self):
        self.name = ''
        self.bankBalance = 1000
        self.amountBet = 0
        self.cardsHolding = []
        self.holdingValue = 0

    def newPlayer(self):
        playerName = input('Enter your name: ')
        self.name = playerName
        print(f'Hello {self.name}. Your balance is {self.bankBalance}.')

    def newBet(self):
        toBet = input('Place your bets! Enter amount: ')
        self.amountBet = toBet

    def showCards(self):
        print(self.cardsHolding)

    def cardsValue(self):
        print(self.holdingValue)

# p = Player()
# p.newPlayer()
