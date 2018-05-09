class Dealer():
    """
    House Dealer, this starts the game. if card count is 17 or greater, they stand.
    Have unlimited balance.
    """
    def __init__(self):
        self.name = 'Dealer'
        self.cardsHolding = []
        self.holdingValue = 0
