class Dealer():
    """BlackJack Dealer class. Should deal until play ready or until hit 21 or over"""
    def __init__(self):
        self.holding = 0
        self.cardsValue = 0


class Player():
    """BlackJack player. Shows amount holding, amount bet, cards value"""
    def __init__(self):
        self.bank = 100
        self.bet = 0
        self.cardsValue = 0

class Deck():
    sym = ['H','C','D','S']
    vals = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
    """The Deck the dealer uses playing the game """
    def __init__(self):
        self.cards = []

    def setUpDeck(self):
        for i in range(len(self.cards)):
            self.cards.pop()
        for s i self.sym:
            for v in vals:
                res = "{x} {y}".format(x = s, y = v)
                self.cards.append(res)

Deck = []
def setUpDeck():
    sym = ['H','C','D','S']
    vals = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
    for s in sym:
        for v in vals:
            res = "{x} {y}".format(x = s, y = v)
            Deck.append(res)

# setUpDeck()
# Deck.pop('H 2')
# print(Deck)
