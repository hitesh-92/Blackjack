class Player():
    """
    Player Class. Holds bankBalance, amountBet, cards held and value of cards
    move - if False = stand else hit
    """
    def __init__(self):
        self.name = ''
        self.bankBalance = 1000
        self.amountBet = 0
        self.cardsHolding = []
        self.holdingValue = 0
        self.move = True


    def newPlayer(self):
        """
        On creating new user. Ask for name and inform of inital balance
        """
        playerName = input('\nWelcome, please enter your name: ')
        self.name = playerName
        print(f'\nHello {self.name}. Your balance is {self.bankBalance}.')


    def newBet(self):
        """
        Prompt player to place new bet.
        Amount should not exceed bankBalance.
        If exceeded, state balance and prompt again
        """
        def completeBet():
            """
            Run when a bet is successfully made
            """
            self.amountBet = toBet
            self.bankBalance -= toBet

        toBet = int(input('\nPlace your bet. Enter amount: '))

        if toBet > self.bankBalance:
            while True:
                print(f"Your current balance: {self.bankBalance}")
                toBet = int(input('Place bet (ensure amount does not exceed balance.): '))
                if toBet <= self.bankBalance:
                    completeBet()
                    break
                else:
                    continue
        completeBet()
        print(f"You have bet: {self.amountBet}. Your balace is: {self.bankBalance}\n")


    def showCards(self):
        """
        Display the cards held by the player
        """
        cards = ''
        for i in self.cardsHolding:
            cards = cards + " |" + i + "| "
        print(f"{self.name} cards: {cards}")


    def cardsValue(self):
        """
        Display the value of the cards being currently held
        """
        print(self.holdingValue)

    def addCard(self, card, value):
        """
        Add card to current holding and adjust holdingValue
        If value==True card is ace. add 1 or 11 depending on count
        """
        if value == True:
            with11 = self.holdingValue + 11
            if with11 >= 21:
                self.holdingValue += 1
            else:
                self.holdingValue += 11

        self.holdingValue += value
        self.cardsHolding.append(card)


    def toPlay(self):
        """
        Ask player if they want to "hit" if true draw card else stand
        Return True or False depending on input
        """
        # print(f"Balance: {self.bankBalance}")
        play = input("\nWould you like another card? (y/n) ")
        if play == 'y':
            return True
        else:
            self.move = False
            return False

    def push(self):
        """
        Game resulted in PUSH. Give the player thier money back
        """
        self.bankBalance += self.amountBet

    def win(self):
        """
        Game resulted with player winning
        """
        # winnings = self.amountBet*2
        # self.bankBalance += winings
        self.bankBalance += (self.amountBet*2)
