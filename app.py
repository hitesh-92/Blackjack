from init import start

print("\nWelcome to BlackJack!\nStarting...")

def run():
    """
    Initalise game,
    setup reset loop if user(s) want to restart
    ask for user name(s)
    """

    while True:
        restart = start()
        if restart == False:
            break
        else:
            continue

run()

print("\nThanks for playing!")