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
        playerName = input('Enter your name: ')
        self.name = playerName
        print(f'Hello {self.name}. Your balance is {self.bankBalance}.')

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

        toBet = int(input('Place your bets! \nEnter amount: '))

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

    def winBet(self):
        """
        Amend bank balace if player wins
        """
        self.bankBalance += (self.amountBet*2)

    def lostBet(self):
        """
        Amend bank balace if player BUST or dealer beats player
        """
        self.bankBalance -= self.amountBet

    def pushBet(self):
        """
        If both players draw wtih equal card values, push bet. The amount they have is given back.
        """

    def showCards(self):
        """
        Display the cards held by the player
        """
        display = '\nPlayer Cards: | '
        for i in self.cardsHolding:
            display += i
            display += ' | '
        if len(display) <= 15:
            display = 'Not holding any cards. Error'

        print(display)


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
            if with11 > 21:
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
        play = input("Do you want another card? ")
        if play == 'y':
            return True
        else:
            self.move = False
            return False
