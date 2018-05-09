class Player():
    """
    Player Class. Holds bankBalance, amountBet, cards held and value of cards
    """
    def __init__(self):
        self.name = ''
        self.bankBalance = 0
        self. amountBet = 0
        self.cardsHolding = []
        self.holdingValue = 0

    def initName(self, playerName):
        self.name = playerName

p = Player()
x = input('Your name? ')
p.initName(x)
print(p.name)
