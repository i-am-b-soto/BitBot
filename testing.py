from datetime import datetime

def get_5_days():
  now = datetime.now()
  for i in range(5):
    print(now.day - (5 - i))

get_5_days()