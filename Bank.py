from GDAX import GDAX

class Bank(object):
	"""docstring foBankme"""
	def __init__(self, USD, Crypto, Coin = 'BTC-USD'):
		self.USD = USD
		self.Crypto = Crypto
		self.dead = False 
		self.coin = Coin

	def current_info(self):
		return  "=======Bank Info: ======== \n" + "Current USD: " + str(self.USD) + "\n" + "Current Crypto: " + str(self.Crypto) + "\n" +"===============" 

	# Buy Crypto based off current price
	def buy(self, price_crypto):
		if self.USD < 25:
			print "Insuffecient USD to make Purchase"
			self.dead = True
			return 

		# The amount used to purchase BTC
		purchase_amount = (self.USD/2.0) - ((self.USD/2.0) * GDAX.fee(self.coin)) 

		# Gained Crypto = purchase_amount / (price of one coin) 
		self.Crypto = self.Crypto + (purchase_amount/(price_crypto * 1.0))

		# Loss USD = USD - Purchase amount
		self.USD = self.USD - purchase_amount

		return (self.current_info())

	# Sell Crypto based off current price
	def sell(self, price_crypto):
		if self.Crypto <= 0:
			print "Insuffecient Crypto to make Sale"
			self.dead = True
			return 

		gain_amount = (self.Crypto * price_crypto) 

		self.USD = self.USD + gain_amount - gain_amount * GDAX.fee(self.coin)

		self.Crypto = 0

		return (self.current_info())

	def spending_money(self):
		return self.USD/2 



		
