from GDAX import GDAX
from datetime import datetime, timedelta

import json

class SMA(object):
	
	"""
		Simple pimple Moving average
		Only in minutes
	"""
	def __init__(self, label, minutes = 15):
		self.GDAX = GDAX(label)
		
		# Current price of the coin
		self.current_price = 0
		
		# Bitch you simple
		self.SMA = 0

		# List of closing prices
		self.closing_prices = []

		# Current index of the closing prices list 
		self.current_index = 0

		# The duration of the ema should always be in minutes
		self.duration = minutes

		# Report our discoveries
		print "Creating " + str(minutes) + " minute SMA"
		self.add_x_minutes(minutes)

	
  	# Calculate duh bitch
  	# Data in json
  	def generate_list(self, data):
  		used_times = {}
		iteration = 0
		for OHLCV in data:
			if  len(self.closing_prices) < self.duration:
				self.closing_prices.append(OHLCV[4])
			else:
				self.closing_prices.pop(0)
				self.closing_prices.append(OHLCV[4])


	# Add up sum dem minutes, add it to the total SMA
	def add_x_minutes(self, num_minutes):
		if num_minutes == 0:
			return;
		
		data = self.GDAX.make_request(datetime.now().replace(microsecond = 0, second = 0) - timedelta(seconds = num_minutes * 60),
		 datetime.now().replace(microsecond = 0, second = 0))
		self.generate_list(data)

	# Geeet summm
	def get_SMA(self):
		closing_price_sum = 0
		for i in range(self.duration):
			closing_price_sum = closing_price_sum + self.closing_prices[i]
		self.SMA = closing_price_sum/self.duration
		return self.SMA

	# get da current price
	def get_current_price(self):
		return self.closing_prices[self.duration -1]

	# Get all dem current prices
	def get_closing_prices(self):
		return self.closing_prices

