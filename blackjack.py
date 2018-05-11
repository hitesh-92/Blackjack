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
        print(f"Balance: {player.bankBalance}")
        player.newBet()
        replay = initGame(player)
        if replay == False:
            #if replay == False. game over.
            #ask to restart
            print(f"\nThe House has won! Better luck next time")
            if player.bankBalance == 0:
                print(f"GAME OVER! {player.name} has no remaining balance")
                break
            continue
        elif replay == None:
            #make case for PUSH
            #add bet back to bank
            print('PUSH! No winner this time')
            player.push()
            continue
        else:
            #if replay == True, still playing
            #add winning or push back to player
            #reset bet amount and cardsholding
            print('You have won!!')
            player.win()
            continue

    return False


def initGame(currentPlayer):
    """
    New Deck, Dealer. Draw cards.
    Make new player as placeholder for actual player
    Return True if won, else False and None if push
    """
    #Register player, dealer and deck
    deck = Deck()
    dealer = Dealer()
    player = currentPlayer

    # Build new deck
    deck.newDeck()

    #Pick cards for player/dealer. 2 each
    for i in range(0,4):
        user = None
        card = deck.pickCard()
        if i == 0 or i == 1:
            user = player
        else:
            user = dealer
        user.addCard(card[0],card[1])


    displayCards(player,dealer)

    #check if both cardsValue == 21:push
    # if either have 21 == win
    # end return True == player won. False == player lost or Push == None
    initCheck = checkStatus(player, dealer, True)

    if initCheck[0] == 'cont':
        pass
    elif initCheck == True:
        print('\n!!!BLACKJACK!!!')
        return initCheck
    elif initCheck == False:
        print('\nBlackJack! The house has won!')


    #holder for result from while loop
    result = None

    #while loop to carry on card draws until
    #dealer >= 17 and player stops or goes BUST
    while True:
        toPlay = player.toPlay()
        if toPlay == True:
            card = deck.pickCard()
            player.addCard(card[0],card[1])
            print(f"\n{player.name} drew card: {card[0]}")
        else:
            player.move = False

        # displayCards(player,dealer)

        #Check if player bust
        if player.holdingValue > 21:
            print(f"\n{player.name} BUST!")
            result = False
            break

        #draw for dealer if .move == True
        if dealer.move == True:
            card = deck.pickCard()
            dealer.addCard(card[0],card[1])
            print(f"\n{dealer.name} drew card: {card[0]}")

        # displayCards(player,dealer)

        #Check if dealer bust
        if dealer.holdingValue > 21:
            print(f"\nDealer BUST!")
            result = True
            break

        displayCards(player, dealer)

        res = checkStatus(player, dealer, False)

        #deal with result
        # if .move for both == False,check again and break.
        if player.move == False and dealer.move == False:
            if res == True:
                result = True
                break
            elif res == False:
                result = False
                break
            elif res == None:
                break

    #return result
    return result


def checkStatus(currentPlayer, currentDealer, init):
    """
    Check current state of game, if there is a winner or push
    Params: player-object, dealer-object, init-bool(true if initial draw)
    init True: return if BlackJack. Push if both BlackJack.
    returns list with 'cont', if so continue play.
    """
    player = currentPlayer
    dealer = currentDealer
    p = player.holdingValue
    d = dealer.holdingValue

    #Case for first draw
    if init == True:
        if p == 21 and d == 21:
            return None
        elif p == 21 and d < 21:
            return True
        elif d == 21 and p < 21:
            return False
        else:
            return ['cont']

    #Case for after drawing card(s)
    if p == d:
        return None
    else:
        return p > d


def displayCards(p,d):
    """
    Shows the players cards
    """
    p.showCards()
    d.showCards()


def appBlackJack():
    while True:
        play = startBlackJack()
        if play == False:
            break

appBlackJack()
