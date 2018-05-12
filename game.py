from deck import Deck
from player import Player
from dealer import Dealer
from display_cards import displayCards

def game(players):
    """
    Start drawing cards.
    Initial draw, 2 each.
    Ask to draw more, if bust add to results list to return
    """

    results = []

    nPlayers = len(players)

    # player1 = players[0]
    # if len(players) > 1:
    #     player2 = players[1]


    deck = Deck()
    deck.newDeck()
    dealer = Dealer()

    #Draw 2 cards each
    for player in range(0,nPlayers+1):
        user = None

        if player == 0:
            user = dealer
        elif player == 1:
            user = players[0]
        elif player == 2:
            user = players[1]

        for card in range(0,2):
            card = deck.pickCard()
            user.addCard(card[0], card[1])

        count = user.cardCount()

        if player == 0:
            if count >= 17:
                user.move = False

        if count == 21:
            user.move = False
            print(f"\n*** {user.name} BlackJack! ***")



    displayCards(players, dealer)

    #select additonal cards for players
    for player in range(0,nPlayers):
        user = None

        if player == 0:
            user = players[0]
        elif player == 1:
            user = players[1]

        while user.move == True:
            res = user.draw()
            if res == True:
                card = deck.pickCard()
                user.addCard(card[0], card[1])
                print(f"\n{user.name} drew card: {card[0]}")
                check = user.cardCount()
                print(f"{user.cards} || {user.name} CHECK: {check}")
                if check > 21:
                    user.move = False
                    user.bust = 'BUST'
                    print(f"\n{user.name} BUST!")
                    break
                displayCards(players,dealer)
                continue
            else:
                user.move = False
                displayCards(players,dealer)
                break

    #dealer picks cards
    while dealer.move == True:
        card = deck.pickCard()
        dealer.addCard(card[0], card[1])
        dCheck = dealer.cardCount()
        print("\n")
        if dCheck == 21:
            dealer.move = False
            break
        elif dCheck > 21:
            dealer.move = False
            print(f"\n{user.name} BUST!")
            break
        displayCards(players,dealer)
        continue

    #compare player(s) to dealer
    dRes = dealer.cardCount()
    
    for player in range(0,nPlayers):
        user = None
        if player == 0:
            user = players[0]
        elif player == 1:
            user = players[1]

        each = user.cardCount()

        if each == dRes:
            results.append(None)
        else:
            res = each > dRes
            results.append(res)

    #remove cards

    return results
