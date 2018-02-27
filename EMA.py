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

  	# Calculate duh bitch
  	# Data in json
  	def generate_list(self, data):
  		used_times = {}
		iteration = 0
		for OHLCV in data:
			try:
				if  len(self.closing_prices) < self.duration:
					self.closing_prices.append(float(OHLCV[4]))
				else:
					self.closing_prices.pop(0)
					self.closing_prices.append(float(OHLCV[4]))
			except Exception as e:
				continue

	# Add up sum dem minutes, add it to the total SMA
	def add_x_minutes(self, num_minutes):
		if num_minutes == 0:
			return;
		
		data = self.GDAX.make_request(datetime.utcnow().replace(microsecond = 0, second = 0) - timedelta(seconds = num_minutes * 60),
		 datetime.utcnow().replace(microsecond = 0, second = 0))
		self.generate_list(data)

	# Geeet summm
	def get_EMA(self):
		self.EMA = []
		self.EMA.append(self.closing_prices[0])
		for i in range(1, len(self.closing_prices)):
			self.EMA.append(self.closing_prices[i] * self.multiplier() + self.EMA[i-1] * (1 - self.multiplier()))
		return self.EMA[len(self.EMA)-1]

	# get da current price
	def get_current_price(self):
		return self.closing_prices[len(self.closing_prices)-1]

	# Get all dem current prices
	def get_closing_prices(self):
		return self.closing_prices

