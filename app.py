from deck import Deck
from player import Player
from dealer import Dealer

# deck = Deck()
# deck.newDeck()
# p = Player()
# p.newPlayer()
# dealer = Dealer()
# print(dealer.name)

# play = True

# while True:
#     if play == True:
#         startBlackJack()
#


def startBlackJack():
    player = Player()
    deck = Deck()
    deck.newDeck()
    dealer = Dealer()

    player.newPlayer()
    

startBlackJack()
