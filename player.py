class Player():
    """
    Player Class. Holds bankBalance, amountBet, cards held and value of cards
    move - if False = stand else hit
    """
    def __init__(self):
        self.name = ''
        self.bankBalance = 1000
        self.amountBet = 0
        self.cards = []
        self.holdingValue = []
        self.move = True
        self.playing = True
        self.bust = ''


    def newName(self, playerName):
        """
        On creating new user. Ask for name and inform of inital balance
        """
        self.name = playerName



    def newBet(self):
        """
        Prompt player to place new bet.
        Amount should not exceed bankBalance.
        If exceeded, state balance and prompt again
        """
        def completeBet(toBet):
            """
            Run when a bet is successfully made
            """
            self.amountBet = toBet
            self.bankBalance -= toBet

        toBet = int(input(f"\n{self.name}'s balance: {self.bankBalance}\n{self.name} place your bet. Enter amount: "))

        if toBet > self.bankBalance:
            while True:
                print(f"Your current balance: {self.bankBalance}")
                toBet = int(input('Place bet (ensure amount does not exceed balance): '))
                if toBet <= self.bankBalance:
                    completeBet(toBet)
                    break
                else:
                    continue
        completeBet(toBet)
        print(f"You have bet: {self.amountBet}. Your balace is: {self.bankBalance}\n")


    def showCards(self):
        """
        Display the cards held by the player
        """
        cards = ''
        for i in self.cards:
            cards = cards + " |" + i + "| "
        print(f"{self.name} cards: {cards}     {self.bust}")


    def addCard(self, card, value):
        """
        # Add card to current holding and adjust holdingValue
        # If value==True card is ace. add 1 or 11 depending on count
        Add cards/cardValue to player
        """
        self.holdingValue.append(value)
        self.cards.append(card)


    def cardCount(self):
        """
        Count the value of cards currently in handself
        Adjust for ace(True)
        """
        ace = 0
        res = 0
        for i in self.holdingValue:
            if i == True:
                ace += 1
            else:
                res += i
        if ace > 0:
            for i in range(0,ace):
                ace = res + 11
                if ace <= 21:
                    res += 11
                else:
                    res += 1

        return res

    def bust(self):
        """
        add 'bust' to self.bust
        """
        # print(f"{self.name} BUST!")
        self.bust += 'BUST'


    def draw(self):
        """
        Ask player if they want to "hit" if true draw card else stand
        Return True or False depending on input
        """
        # print(f"Balance: {self.bankBalance}")
        play = input(f"\n{self.name}\nFor hit (enter 'y') or Stand (enter 'n'): ")
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
        self.bankBalance += (self.amountBet*2)

    def reset(self):
        """
        If round complete, reset cards to not hold and reset holdingValue
        """
        self.cardsHolding = []
        self.holdingValue = 0
