class Dealer():
    """
    House Dealer, this starts the game. if card count is 17 or greater, they stand.
    Have unlimited balance.
    move - if False = stand else hit
    """
    def __init__(self):
        self.name = 'Dealer'
        self.cardsHolding = []
        self.holdingValue = []
        self.move = True
        self.bust = ''

    def addCard(self, card, value):
        """
        # Add card to current holding and adjust holdingValue
        # If value==True card is ace. add 1 or 11 depending on count
        """
        self.cardsHolding.append(card)
        self.holdingValue.append(value)


    def cardCount(self):
        """
        Count the value of cards currently in handself
        Adjust for ace(True)
        """
        ace = 0
        res = 0
        for i in self.holdingValue:
            if i == True:
                ace += 1
            else:
                res += i
        if ace > 0:
            for i in range(0,ace):
                ace = res + 11
                if ace <= 21:
                    res += 11
                else:
                    res += 1
        return res


    def showCards(self):
        """
        Display the cards held by the dealer
        """
        cards = ''
        for i in self.cardsHolding:
            cards = cards + " |" + i + "| "
        print(f"{self.name} cards: {cards}     {self.bust}")

    def bust(self):
        """
        If dealer goes BUST drawing cards
        """
        self.bust = 'BUST'
