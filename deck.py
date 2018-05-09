from random import randint
# print(randint(0,9))


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
        """
        Returns amount of cards currently in deck
        """
        return len(self.currentCards)


    def pickCard(self):
        """
        Picks a random number, depending on the amount of cards.
        Pops card from the list of currentCards and returns the card values
        """
        nCards = len(self.currentCards)-1
        nPick = randint(0,nCards)
        card = self.currentCards[nPick]
        print(card)
        return self.currentCards.pop(nPick)


    def cardValue(self,card):
        """
        Find the value of the card and return and int.
        Exception: 'Ace'. This has vlaue of 1 or 11 depending on holders cards.
        'Ace' will return bool(True). Deal with accordingly
        """
        value = card[2::]
        # print(type(value))
        # print(len(value))

        if len(value) == 3:
            # print('Ace')
            return True
        elif len(value) == 1:
            # print(int(value))
            return int(value)
        else:
            # print(10)
            return 10


# deck = Deck()
# deck.newDeck()

#Prints cards currently in deck
# print(deck.currentCards)

#Print amount of cards currently in deck
# print(deck.cardCount())

#Pick a random card
# deck.pickCard()

#Find value of card
# x = deck.pickCard()
# deck.cardValue(x)
