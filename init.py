from player import Player
from game import game

def start():
    """
    Start by asking for user name(s),
    ask for bet and then into game() to continue
    game() returns list containing player(s) result(s)
    """

    #set up players
    players = []

    name1 = input(f"\nAdding player. Please enter your name: ")
    player1 = Player(name1)
    players.append(player1)

    ask = input("\nWould you like to add another player? (y/n): ")

    if ask == 'y':
        name2 = input(f"\nAdding player 2. Please enter your name: ")
        player2 = Player(name2)
        players.append(player2)

    #ask player(s) to place bet
    #if balance == 0: playing=False
    #pop if playing==False


    #loop to play until player(s) both balance = 0
    while True:

        nPlayers = len(players)

        for i in range(0,nPlayers):
            players[i].placeBet()

        #play game()
        #returns None=push, True=win, False=lost
        results = game(players)

        for res in results:

            for player in players:

                if res == None:
                    #PUSH
                    player.playerPush()
                    player.pReset()

                elif res == True:
                    #WIN
                    player.playerWon()
                    player.pReset()

                else:
                    #LOST
                    #if balance==0: pop and msg player removed
                    player.playerLost()
                    player.pReset()

                    if player.playing == False:
                        name = player.name
                        print(f"\n{name} has no remaing balance; removed from game!")
                        players.pop(0)


        # for player in players:
        #     if player.playing == False:
        #         print('\n***POPPING***')
        #         players.pop(0)


        if len(players) == 0:
            print("\nBetter Luck Next Time!")
            break

        continue


    #ask to play again
    #if y: return True
    #else False
    ask = input("\nWould you like to play again? (y/n)")
    if ask == 'y':
        return True
    else:
        return False



