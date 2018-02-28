class Bank(object):
	"""docstring foBankme"""
	def __init__(self, USD, Crypto, File = "Purchasing.txt"):
		self.USD = USD
		self.Crypto = Crypto
		self.file = File
		self.dead = False 

	def current_info(self):
		return  "=============== \n" + "Current USD: " + str(self.USD) + "\n" + "Current Crypto: " + str(self.Crypto) + "\n" +"===============" 

	def buy(self, price_crypto):
		if self.USD < 25:
			print "Insuffecient USD to make Purchase"
			self.dead = True
			return 
		self.Crypto = self.Crypto + ((self.USD / 2.0)/(price_crypto * 1.0))
		self.USD = self.USD - (self.USD/2.0) - ((self.USD/2.0) * 0.003) 
		print(self.current_info())

	def sell(self, price_crypto):
		if self.Crypto <= 0:
			print "Insuffecient Crypto to make Sale"
			self.dead = True
			return 
		self.USD = self.USD + (self.Crypto - self.Crypto * 0.003) * price_crypto
		self.Crypto = 0
		print(self.current_info())



		
