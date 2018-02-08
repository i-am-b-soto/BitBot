from datetime import datetime, timedelta
import debugging
import time
from Bank import Bank
from Decision import Decision
from EMA import EMA
from SMA import SMA

Bank = Bank(1000, 0)
Decision = Decision(Bank)
SMA = SMA('ETH-USD')
EMA = EMA('ETH-USD')
sleep_time = 4

def get_real_time_trading():
  global SMA, EMA, sleep_time
  while(True):    
    SMA.add_x_minutes(1)
    EMA.add_x_minutes(1)
    Decision.make_decision(EMA.get_EMA(), SMA.get_SMA(), SMA.get_current_price())
    
    for i in range(sleep_time):
      time.sleep(80/sleep_time)
      print " . ", 
    print ""


get_real_time_trading()

