from deck import Deck
from player import Player
from dealer import Dealer
from add_players import addPlayers
from display_cards import displayCards
from game import game

players = addPlayers()
nPlayers = len(players)


while True:

    for i in range(0,nPlayers):
        if players[i].playing == True:
            #Place bets
            players[i].newBet()

    result = game(players)
    res = len(result)

    for player in range(0,nPlayers):
        user = None

        if player == 0:
            user = players[0]
        else:
            user = players[1]

        print('---------------')

        if result[player] == None:
            user.push()
            print(f"\n{user.name}. PUSH")
        elif result[player] == True:
            user.win()
            print(f"{user.name}. You Have Won!")
        else:
            print(f"{user.name}. Better luck next time!")
            if user.bankBalance == 0:
                user.playing = False
                print(f"{user.name} has no more money. Hope to you soon!")

        print('---------------')


        # if nPlayers > 1:
        #     if players[0].playing == False and players[1].playing == False:
        #         break
        # if players[0].playing == False:
        #     break
