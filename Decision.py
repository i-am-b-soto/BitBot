from Bank import Bank
from datetime import datetime
import sys

from GDAX import GDAX

class Decision(object):
	""""""
	def __init__(self, bank, coin = 'BTC-USD', output_file = "output_file.txt"):

		# 0 = start, 1 = buy, 2 = sell  
		self.state = 0

		# Bank information
		self.bank = bank

		# Price previously purchased crypto
		self.bought_at = 0

		# The coin-USD pair
		self.coin = coin

		# The name of the file to putput info to
		self.output_file = output_file

	def sell(self, price_crypto):
		if self.state !=2 :
			print "Error, trying to sell on a buy"  
			return

		print " Selling at: " + str(price_crypto)
		self.bank.sell(price_crypto)

		if self.bank.dead:
			print "Bank is dead!!"
			sys.exit(0)

		self.bought_at = 0
		now = datetime.now()
		samantha = open(self.output_file, "a")
		samantha.write('===Sold at :  {day:02d}-{hour:02d}-{second:02d}===\n'.format(day = now.day, hour = now.hour, second = now.second))
		samantha.write(self.bank.current_info())
		samantha.close()

	def buy(self, price_crypto):
		
		if self.state !=1:
			return "Error, trying to buy on a sell"

		print " Buying at: " + str(price_crypto)
		self.bank.buy(price_crypto)

		if self.bank.dead:
			print "Bank is dead!!"
			sys.exit(0)

		self.bought_at = price_crypto
		now = datetime.now()
		samantha = open(self.output_file, "a")
		samantha.write('===Bought at : \n {day:02d}-{hour:02d}-{second:02d}===\n'.format(day = now.day, hour = now.hour, second = now.second))
		samantha.write(self.bank.current_info())
		samantha.close()

	def get_delta(self):
		return 0.000

	def start_state(self, EMA, SMA, price_crypto):
		delta = self.get_delta()
		if EMA < (SMA - delta * SMA):
			# Switch to buy state 
			self.state = 1
			return  

	# Waiting to buy (EMA > SMA)
	def wait_to_buy(self, EMA, SMA, price_crypto):
		delta = self.get_delta()
		if EMA > (SMA + SMA*delta):
			self.buy(price_crypto)
			self.state = 2
			return 	

	# Waiting to sell (EMA < SMA)
	def wait_to_sell(self, EMA, SMA, price_crypto):
		delta = self.get_delta()
		if EMA < (SMA - SMA*delta):
			if price_crypto > self.bought_at:
				
				self.sell(price_crypto)
				self.state = 1
				return


	def get_state(self):
		return self.state

	# Think carefully
	def make_decision(self, EMA, SMA, price_crypto):
		
		if self.state == 0 : 
			self.start_state(EMA, SMA, price_crypto),
		if self.state == 1 : 
			self.wait_to_buy(EMA, SMA, price_crypto),
		if self.state == 2 : 
			self.wait_to_sell(EMA, SMA, price_crypto)
		
	


		
		