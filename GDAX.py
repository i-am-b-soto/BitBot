from datetime import datetime, timedelta
from time import sleep
import debugging
import time

import json
import requests

class GDAX(object):
  """
  Fetch Deh Candles 
  """
 
  def __init__(self, coin):

    self.coin = coin
    self.uri = 'https://api.gdax.com/products/'+coin+ '/candles'

  @staticmethod
  def __date_to_iso8601(date):
    return '{year}-{month:02d}-{day:02d}T{hour:02d}:{minute:02d}:{second:02d}'.format(
        year=date.year,
        month=date.month,
        day=date.day,
        hour=date.hour,
        minute=date.minute,
        second=date.second)

  """
    Start - datetime object
    End - datetime object
    granularity (Should be 60)
  """
  def make_request(self, start, end, granularity = 60):

    for retry in xrange(0, 3):
      response = requests.get(self.uri, params = {
        'start': self.__date_to_iso8601(start),
        'end': self.__date_to_iso8601(end),
        'granularity': granularity  # granularity is in seconds.
      })

      try:
        result = sorted(response.json(), key=lambda x: x[0])
        return result
      except Exception as e:
        pass
      
    return "{}"


