from Bank import Bank
from datetime import datetime
import sys

class Decision(object):
	""""""
	def __init__(self, bank):
		self.has_bought = False
		self.bank = bank

	def make_decision(self, EMA, SMA, price_crypto):
		
		# we are looking for an opportunity to sell
		if self.has_bought:
			if EMA <= SMA:
				print " Making purchase at: " + str(price_crypto)
				print " Time: "
				print datetime.now()
				self.bank.sell(price_crypto)
				self.has_bought = False
			else:
				print "Holding"

		# we are looking for an opportunity to buy
		else:
			if EMA >= SMA:
				print "Purchasing at: " + str(price_crypto)
				print "Time: " 
				print datetime.now()
				self.bank.buy(price_crypto)
				self.has_bought = True
			else:
				print "Holding"

		if self.bank.dead:
			sys.exit("Bank is out of resources, halting program")

		return 
		