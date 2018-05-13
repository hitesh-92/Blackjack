from player import Player
from dealer import Dealer

def check(players,dealer):
	"""
	Final results check
	return list, True=won False=lost None=push
	"""
	def checking(p,d):
		# d>21 and p<=21
		# d<=21 and p>21
		# d == p
		# d>p or d<p
		if d > 21 and p <= 21:
			return True
		elif d <= 21 and p > 21:
			return False
		elif p == d:
			return None
		else:
			return p > d


	res = []

	d = dealer.countCards()

	player1 = players[0].countCards()
	p1 = checking(player1,d)
	res.append(p1)	

	if len(players) > 1:

		player2 = players[1].countCards()
		p2 = checking(player2,d)
		res.append(p2)

	return res