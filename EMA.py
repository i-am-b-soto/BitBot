from GDAX import GDAX
from datetime import datetime, timedelta
import pandas

class EMA(object):
	
	"""
		Exponential Moving average
		Only in minutes
	"""
	def __init__(self, label, minutes = 10):
		self.GDAX = GDAX(label)
		
		# Current price of the coin
		self.current_price = 0
		
		# List of EMA's throughout the minutes
		self.EMA = []

		# List of closing prices
		self.closing_prices = []

		# Current index of the closing prices list 
		self.current_index = 0

		# The duration of the ema should always be in minutes
		self.duration = minutes


		print "Creating " + str(minutes) + " minute EMA"
		self.add_x_minutes(minutes)

	# get da current price
	def get_current_price(self):
		return self.closing_prices[self.duration -1]

	# Should be a lamda equation
  	def multiplier(self):
  		return (2/(self.duration + 1.0))
	
	# Add de modda fukka to da list
	def add_to_list(self, closing_price):
		if (self.current_index < self.duration):
			self.closing_prices.append(closing_price)
			self.current_index = self.current_index + 1
		else:
			self.closing_prices.pop(0)
			self.closing_prices.append(closing_price)

  	# Calculate duh bitch
  	def generate_list(self, data):
		data_frame = pandas.DataFrame(data=data, columns=['time', 'low', 'high', 'open', 'close', 'volume'])
		data_frame.set_index('time', inplace=True)
		data_frame = data_frame[~data_frame.index.duplicated(keep='first')]

		close_price_to_add = 0
		for close_price in data_frame['close']:
			close_price_to_add = close_price

		self.add_to_list(close_price_to_add)

	# careful
	def calculate(self):
		self.EMA = []
		self.EMA.append(self.closing_prices[0])
		for i in range(1, self.duration):
			self.EMA.append(self.closing_prices[i] * self.multiplier() + self.EMA[i-1] * (1 - self.multiplier()))

	# Add up sum dem minutes
	def add_x_minutes(self, num_minutes):
		if num_minutes == 0:
			return;
		now = datetime.now()
		data = self.GDAX.fetch(datetime.now() - timedelta(seconds = num_minutes * 60), datetime.now(), 1)
		self.generate_list(data)
		self.calculate()

	# Geeet summm
	def get_EMA(self):
		return self.EMA[self.duration - 1]


