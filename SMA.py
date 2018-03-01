from GDAX import GDAX
from datetime import datetime, timedelta

import json

class SMA(object):
	
	"""
		Simple pimple Moving average
		Only in minutes
	"""
	def __init__(self, label, minutes = 15, base_time = "Current"):
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

		# Base time in minutes
		self.base_time = base_time

		# Report our discoveries
		print "Creating " + str(minutes) + " minute SMA"
		self.add_x_minutes(minutes)

	
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

	# returns base time object based off inputted base time
  	def get_base_time(self, incr = 0):
  		if self.base_time == "Current":
  			return datetime.utcnow()
  		else:
  			self.base_time = self.base_time + timedelta(minutes = incr)
  			return self.base_time

	# Add up sum dem minutes
	def add_x_minutes(self, num_minutes):
		if num_minutes == 0:
			return;
		
		data = self.GDAX.make_request(self.get_base_time(num_minutes).replace(microsecond = 0, second = 0) - timedelta(seconds = num_minutes * 60),
		 self.get_base_time().replace(microsecond = 0, second = 0))
				
		if data:
			self.generate_list(data)

	# Geeet summm
	def get_SMA(self):
		closing_price_sum = 0
		for i in range(len(self.closing_prices)):
			closing_price_sum = closing_price_sum + self.closing_prices[i]
		self.SMA = closing_price_sum/self.duration
		return self.SMA

	# get da current price
	def get_current_price(self):
		return self.closing_prices[len(self.closing_prices)-1]

	# Get all dem current prices
	def get_closing_prices(self):
		return self.closing_prices

