from datetime import datetime, timedelta
import debugging
import time
from Bank import Bank
from Decision import Decision
from EMA import EMA
from SMA import SMA

# Create a bank with 1,000 USD, 0 Crypto
Bank = Bank(1000, 0, "BankFile1.txt")
Decision = Decision(Bank)
SMA = SMA('BTC-USD')
EMA = EMA('BTC-USD')


def run():
  global SMA, EMA, sleep_time
    
  time.sleep(60)
  while (True):
    print datetime.now()

    SMA.add_x_minutes(1)
    print "Current SMA: " + str(SMA.get_SMA())

    EMA.add_x_minutes(1)
    print "Current EMA: " + str(EMA.get_EMA())

    print "Current Price: " + str(SMA.get_current_price()) 

    Decision.make_decision(EMA.get_EMA(), SMA.get_SMA(), SMA.get_current_price())
    time.sleep(60)

run()
