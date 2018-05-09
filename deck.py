from random import randint

class Deck():
    """
    Deck of cards, containing 52 cards with 4 suits containing 2-A
    """

    def __init__(self):
        self.currentCards = []


    def newDeck(self):
        """
        Set up new deck of cards with all 52 cards. Appends to currentCards
        """
        suits = ['H','D','S','C']
        values = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']

        for suit in suits:
            #Prints 4 suits letters
            # print(suit)

            for value in values:
                #Prints all values with each suit
                # print(f"{suit} {value}")
                self.currentCards.append(f"{suit} {value}")

    def cardCount(self):
        return len(self.currentCards)






deck = Deck()
deck.newDeck()

#Prints cards currently in deck
# print(deck.currentCards)

#Print amount of cards currently in deck
# print(deck.cardCount())

#Pick a random card

print(randint(0,9))
