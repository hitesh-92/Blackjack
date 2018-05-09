def Deck():
    """
    Deck of cards, containing 52 cards with 4 suits containing 2-A
    """

    suits = ['H','D','S','C']
    values = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']


    def __init__(self):
        currentCards = []

    def newDeck(self):
        for i in range(len(suits)):
            print(i)

deck = Deck()

print(deck.currentCards)
