from player import Player

def addPlayers():
    """
    Ask for players and init game
    """
    print("\nPlaying BlackJack!")

    #Add players (1 or and 2)
    names = []
    players = []

    player = input("\nAdding player: Please enter your name:  ")
    names.append(player)
    while True:
        ask = input("\nWould you like to add another player (y/n): ")
        if ask == 'y':
            player = input("\nAdding player 2: Please enter your name:  ")
            names.append(player)
            break
        else:
            break

    player1 = Player()
    player1.name = names[0]
    players.append(player1)

    if len(names) > 1:
        player2 = Player()
        player2.name = names[1]
        players.append(player2)

    return players
