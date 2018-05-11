from deck import Deck
from player import Player
from dealer import Dealer


def startBlackJack():
    """
    Initiate game. Set up Player.
    """
    player = Player()
    player.newPlayer()

    playGame = True

    while True:
        player.newBet()
        replay = initGame(player)
        if replay == False:
            #if replay == False. game over.
            break
        elif replay == None:
            #make case for PUSH
            pass
        else:
            #if replay == True, still playing
            #add winning or push back to player
            #reset bet amount and cardsholding
            continue


def initGame(currentPlayer):
    """
    New Deck, Dealer. Draw cards.
    Make new player as placeholder for actual player
    Return True if won, else False and None if push
    """
    deck = Deck()
    dealer = Dealer()
    player = currentPlayer

    deck.newDeck()

    for i in range(0,4):
        user = None
        card = deck.pickCard()
        if i == 0 or i == 1:
            user = player
        else:
            user = dealer
        user.addCard(card[0],card[1])

    print(player.cardsHolding)
    print(dealer.cardsHolding)
    player.showCards()
    # dealer.showCards()








startBlackJack()
