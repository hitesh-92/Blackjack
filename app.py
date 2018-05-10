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
    print("Playing BlackJack!\n")
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

    #Inital round player
    card1 = deck.pickCard()
    player.addCard(card1[0],card1[1])
    card2 = deck.pickCard()
    player.addCard(card2[0],card2[1])

    #Initial round dealer
    card3 = deck.pickCard()
    dealer.addCard(card3[0],card3[1])
    card4 = deck.pickCard()
    dealer.addCard(card4[0],card4[1])

    while True:
        player.showCards()
        dealer.showCards()

        hit = input('\nWould you like another card? (y/n):  ')

        if hit == 'n':
            player.move = False
        else:
            hCard = deck.pickCard()
            player.addCard(hCard[0],hCard[1])

        if dealer.move == True:
            dCard = deck.pickCard()
            dealer.addCard(dCard[0],dCard[1])

        print('\nCards Delt\n')

        result = bustCheck(player.holdingValue, dealer.holdingValue)




        #check .move both False. if both false break


    # print('player')
    # print(player.cardsHolding)
    # print(player.holdingValue)
    # print('dealer')
    # print(dealer.cardsHolding)
    # print(dealer.holdingValue)
    # print(dealer.move)

# def show(p, d):
#     print('Player:')
#     print(f"{p.name}\n{p.bankBalance}\n{p.amountBet}\n{p.cardsHolding}\n{p.holdingValue}\n")
#     print('Dealer')
#     print(f"")


def winCheck(p1,d):
    if p1 > 21:
        return


startBlackJack()
