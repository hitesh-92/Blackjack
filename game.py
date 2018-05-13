from deck import Deck
from player import Player
from dealer import Dealer
from check import check

def game(players):
	"""
	Takes 1 param, should be list of players
	Set up deck
	Set up dealer
	Draw 2 cards each,
	if 21 skip player hit/stand
	if on draw cards==21 end turn
	after players done, deal dealer
	compare cards and end and return to init.py 
	"""

	def display(players,dealer):
		"""
		Dispay all players cards
		"""
		players[0].displayCards()
		if len(players)>1:
			players[1].displayCards()
		dealer.displayCards()


	#set up deck and dealer
	deck = Deck()
	dealer = Dealer()
	deck.newDeck()

	#init cardPick. pick 2 each
	nPlayers = len(players)

	for i in range(0,nPlayers):
		cards = deck.pickCard(True)
		players[i].addCard(cards[0][0],cards[0][1])
		players[i].addCard(cards[1][0],cards[1][1])

		initCheck = players[i].countCards()

		if initCheck == 21:
			name = players[i].name
			print(f"*** {name} hit BlackJack! ***")
			players[i].move = False

	#dealers pick
	dCards = deck.pickCard(True)
	dealer.addCard(dCards[0][0],dCards[0][1])
	dealer.addCard(dCards[1][0],dCards[1][1])

	dMove = dealer.countCards()
	if dMove >= 17:
		dealer.move = False


	display(players,dealer)

	#ask players for addtional cards
	for i in range(0,nPlayers):
		if players[i].move == True:

			while True:
				ask = players[i].cardAsk()
				if ask == True:
					card = deck.pickCard(False)
					players[i].addCard(card[0][0],card[0][1])

					check1 = players[i].countCards()
					if check1 > 21:
						players[i].move = False
						players[i].playerBust()
						display(players,dealer)
						break
					elif check1 == 21:
						players[i].move = False
						display(players,dealer)
						break
				else:
					players[i].move = False
					break
				display(players,dealer)
				continue

	bothBust = 0
	for i in range(0, nPlayers):
		if players[i].bust == 'BUST':
			bothBust += 1

	#pick card for dealer until >= 17
	if bothBust < 1:
		if dealer.move == True:
			while True:

				card = deck.pickCard(False)
				dealer.addCard(card[0][0],card[0][1])

				dCheck = dealer.countCards()

				if dCheck > 21:
					dealer.dealerBust()
					dealer.move = False
					break
				elif dCheck == 21:
					break
				elif dCheck >= 17:
					break

	display(players,dealer)


	#check results
	results = check(players,dealer)
	# print('\nRESULTS:')
	# print(results)

	return results




