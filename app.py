from deck import Deck
from player import Player
from dealer import Dealer
from add_players import addPlayers
from display_cards import displayCards
from game import game

# def start():
#     """
#     Before game begins get users
#     """

players = addPlayers()
nPlayers = len(players)

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

    if result[player] == None:
        user.push()
        print(f"\n{user.name}. PUSH")
    elif result[player] == True:
        user.win()
        print(f"{user.name}. You Have Won!")
    else:
        print(f"{user.name}. Better luck next time!")
