class Player():
    """
    Class new player.
    Name, balance, bet, cards
    """

    def __init__(self, playerName):
        self.name = playerName
        self.balance = 1000
        self.bet = 0
        self.cards = []
        self.values = []
        self.bust = ''
        self.move = True
        self.playing = True

    def pReset(self):
        """
        Reset for another round
        """
        self.bet = 0
        self.cards = []
        self.values = []
        self.bust = ''
        self.move = True


    def placeBet(self):
        """
        Player decideds bet amount,
        cannot exceed balance
        """

        print(f"\nCurrent balance: {self.balance}")
        amount = int(input(f"{self.name} please enter amount to bet: "))

        if amount > self.balance or amount == 0:
            while True:
                print(f"\nPlease enter amount up to or including {self.balance}: ")
                amount = int(input(f"{self.name} please enter amount to bet bet: "))
                if amount <= self.balance and amount > 0:
                    break
                else:
                    continue
        self.bet = amount
        self.balance -= amount
        print(f"You have bet: {self.bet}. Your balace is: {self.balance}\n")



    def addCard(self,card, value):
        """
        Appends card param to cards
        """
        self.cards.append(card)
        self.values.append(value)


    def countCards(self):
        """
        Return values total
        Adjust if ace(True)
        if value >21: return None == BUST
        """
        ace = 0
        res = 0

        for i in self.values:
            if i == True:
                ace += 1
            else:
                res += i

        if ace > 0:
            for i in range(0,ace):
                a = res + 11
                if a <= 21:
                    res += 11
                else:
                    res += 1
        
        return res


    def displayCards(self):
        """
        Dispay the cards held by player
        """
        cards = ''
        for i in self.cards:
            cards = cards + "  |" + i + "| "
        print(f"{self.name} holding: {cards}     {self.bust}")


    def cardAsk(self):
        """
        Ask player if they want additional card
        """
        ask = input(f"\n{self.name}, HIT (y) or STAND (n):  ")
        if ask == 'y':
            return True
        else:
            return False


    def playerBust(self):
        self.bust = 'BUST'


    def playerPush(self):
        self.balance += self.bet
        print(f"\n{self.name} PUSH | Balance: {self.balance}")

    def playerWon(self):
        self.balance += self.bet*2
        print(f"\n{self.name} WON | Balance: {self.balance}")

    def playerLost(self):
        print(f"\n{self.name} LOST | Balance: {self.balance}")
        if self.balance == 0:
            self.playing = False

