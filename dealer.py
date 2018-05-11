class Dealer():
    """
    House Dealer, this starts the game. if card count is 17 or greater, they stand.
    Have unlimited balance.
    move - if False = stand else hit
    """
    def __init__(self):
        self.name = 'Dealer'
        self.cardsHolding = []
        self.holdingValue = 0
        self.move = True

    def addCard(self, card, value):
        """
        Add card to current holding and adjust holdingValue
        If value==True card is ace. add 1 or 11 depending on count
        """
        if value == True:
            with11 = self.holdingValue + 11
            if with11 > 21:
                self.holdingValue += 1
            else:
                self.holdingValue += 11

        self.holdingValue += value
        self.cardsHolding.append(card)

        if self.holdingValue >= 17:
            self.move = False

    def showCards(self):
        """
        Display the cards held by the dealer
        """
        cards = ''
        for i in self.cardsHolding:
            cards = cards + " |" + i + "| "
        print(f"{self.name} cards: {cards}")
