from datetime import datetime, timedelta
import debugging
import time
from Bank import Bank
from Decision import Decision
from EMA import EMA
from SMA import SMA

"""
Run Bitbot against Historical Data from 24 hours ago
"""
# Num minutes in a day 
hours = 24
num_iterations = hours * 60 

# Create a bank with 1,000 USD, 0 Crypto
Bank = Bank(1000, 0)
decision = Decision(Bank)
SMA = SMA('BTC-USD', base_time = (datetime.utcnow() - timedelta(hours = hours)))
EMA = EMA('BTC-USD', base_time = (datetime.utcnow() - timedelta(hours = hours)))


def run():
  global decision, SMA, EMA

  iteration = 0
  state = 0
  while (iteration < num_iterations):
    EMA.add_x_minutes(1)
    SMA.add_x_minutes(1)
    decision.make_decision(EMA.get_EMA(), SMA.get_SMA(), SMA.get_current_price())


    iteration = iteration + 1

    # To avoid being blocked from the server
    time.sleep(1)



run()