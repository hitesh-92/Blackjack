from player import Player
from dealer import Dealer

def displayCards(p,d):
    """
    prints cards each player holds
    """
    p[0].showCards()

    if len(p) > 1:
        p[1].showCards()

    d.showCards()
