class Dealer():
	"""
	dealer
	"""

	def __init__(self):
		self.name = 'Dealer'
		self.cards = []
		self.values = []
		self.move = True
		self.bust = ''

	
	def addCard(self,card, value):
		"""
		Appends card param to cards
		"""
		self.cards.append(card)
		self.values.append(value)


	def countCards(self):
		"""
		Return values total
		Adjust for ace
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
		Display cards held
		"""
		cards = ''
		for i in self.cards:
			cards = cards + " |" + i + "| "
		print(f"{self.name} holding: {cards}     {self.bust}")


	def dealerBust(self):
		self.bust = 'BUST'