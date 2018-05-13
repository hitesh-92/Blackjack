from random import randint
# print(randint(0,9))

class Deck():
	"""
	Deck the game uses
	Should contain 52 cards
	"""

	def __init__(self):
		self.cards = []


	def newDeck(self):
		suits = ['H','D','S','C']
		values = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']

		for suit in suits:
			for value in values:
				self.cards.append(f"{suit} {value}")


	def pickCard(self, init):
		"""
		Pick randint from len(cards)
		Select card and pop
		init = initial pick (2cards)
		if init==True: pick2 cards else 1
		"""
		if init == True:
			count = 2
		else:
			count = 1

		res = []

		while True:
			nCards = len(self.cards)-1
			nPick = randint(0,nCards)
			card = self.cards[nPick]
			cardVal = None

			value = card[2::]
			if len(value) == 3:
				cardVal = True
			elif len(value) == 1:
				cardVal = int(value)
			else:
				cardVal = 10

			card = self.cards.pop(nPick)

			each = [card, cardVal]
			res.append(each)

			count -= 1
			if count == 0:
				break
		
		if init == False:
			c = (res[0][0])
			print(f"\nPicked card: {c}")

		return res


	


# x = Deck()
# x.newDeck()
# c=x.pickCard(True)
# print(c)
