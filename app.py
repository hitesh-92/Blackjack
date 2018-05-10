from deck import Deck
from player import Player
from dealer import Dealer

# #Place end of code at end
# play = True
# while True:
#     if play == True:
#         startBlackJack()


def startBlackJack():
    """
    Start game. Register player, dealer and deck.
    Ask player for name.
    """
    player = Player()
    deck = Deck()
    dealer = Dealer()

    deck.newDeck()
    player.newPlayer()

    playGame(player, dealer, deck)




def playGame(p, d, de):
    """
    p = player. d = dealer. de = deck
    """
    player = p
    dealer = d
    deck = de

    #First round
    player.newBet()

    #Inital player round
    card1 = deck.pickCard()
    player.addCard(card1[0],card1[1])
    card2 = deck.pickCard()
    player.addCard(card2[0],card2[1])

    #Initial dealer round
    card3 = deck.pickCard()
    dealer.addCard(card3[0],card3[1])
    card4 = deck.pickCard()
    dealer.addCard(card4[0],card4[1])

    print('player')
    print(player.cardsHolding)
    print(player.holdingValue)
    print('dealer')
    print(dealer.cardsHolding)
    print(dealer.holdingValue)








startBlackJack()
