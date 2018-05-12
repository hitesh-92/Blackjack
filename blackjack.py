from deck import Deck
from player import Player
from dealer import Dealer


def startBlackJack():
    """
    Initiate game. Set up Player.
    """
    player = Player()
    player.newPlayer()

    while True:
        # print(f"Balance: {player.bankBalance}")
        player.newBet()
        replay = initGame(player)
        player.reset()
        if replay == False:
            #if replay == False. game over.
            #ask to restart
            print(f"\nThe House has won! Better luck next time\n")

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




def results(res):
    """
    List as param, [0] = player, [1]= dealer
    find result.
    if player won retuen true, if lost return false, tie(push) return None
    """
    p = res[0]
    d = res[1]
    if p == d:
        return None
    else:
        return p > d



def initGame(currentPlayer):
        """
        New Deck, Dealer. Draw cards.
        Make new player as placeholder for actual player
        Return True if won, else False and None if push
        """
        def count(player,dealer):
            """
            Return list with value of cards held for player,dealer
            """
            p = player.cardCount()
            d = dealer.cardCount()
            return [p,d]

        def displayCards(p,d):
            """
            Shows the players cards
            """
            p.showCards()
            d.showCards()

        def results(res):
            """
            List as param, [0] = player, [1]= dealer
            find result.
            if player won retuen true, if lost return false, tie(push) return None
            """
            p = res[0]
            d = res[1]
            if p == d:
                return None
            else:
                return p > d


        #Register player, dealer and deck
        deck = Deck()
        dealer = Dealer()
        player = currentPlayer

        # Build new deck
        deck.newDeck()

        #Pick cards for player/dealer. 2 each
        for i in range(0,4):
            card = deck.pickCard()
            user = None
            if i == 0 or i == 1:
                user = player
            else:
                user = dealer
            user.addCard(card[0],card[1])

        displayCards(player,dealer)

        #if both blackjack return None
        #if player blackjack return True
        #if dealer blackjack return False
        check = count(player,dealer)
        if check[0] == 21 and check[1] == 21:
            return None

        #player 'hit' until 'stand'
        while player.move == True:
            if check[0] == 21:
                player.move = False
                break
            play = player.toPlay()
            if play == True:
                card = deck.pickCard()
                player.addCard(card[0],card[1])
                print(f"{player.name} drew card: {card[0]}")
                displayCards(player,dealer)
                count = player.cardCount()
                if count > 21:
                    return None
                if count == 21:
                    player.move = False
                    break
                continue
            else:
                player.move = False
                break

        while dealer.move == True:
            if check[1] == 21:
                dealer.move = False
                break
            while True:
                count = dealer.cardCount()
                if count >= 17:
                    dealer.move = False
                    break
                else:
                    card = deck.pickCard()
                    dealer.addCard(card[0],card[1])
                    print(f"Dealer drew card: {card[0]}")
                    displayCards(player,dealer)
                    continue
            # break

        check = count(player,dealer)
        res = results(check)
        return res






def appBlackJack():
    while True:
        play = startBlackJack()
        if play == False:
            res = input('Play again? (y)')
            if res == 'y':
                continue
            else:
                break

appBlackJack()
