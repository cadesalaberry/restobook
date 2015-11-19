# Because eve is not made to modify code programatically
# (see filters http://python-eve.org/config.html)
# Here is a sample using a list of reservations and restaurants


from datetime import datetime
from mock import reservations


def get_all_reservations_from_restaurant(reservations=reservations, restaurant_id=""):

  result = [r for r in reservations if r['restaurant_id'] is restaurant_id]

  return result

def get_all_reservations_from_day(reservations=reservations, day="2015-01-01 03:55:00"):

  pass

"""
Query looks like:
date=2015-01-01&time=03%3A55&headcount=3
"""
def search(date='2015-01-01', time='03:55', headcount=3, restaurant_id="23"):

  dtime = date + ' ' + time

  desired_time = datetime.strptime(dtime, '%Y-%m-%d %I:%M')

  print desired_time

  res = get_all_reservations_from_restaurant(restaurant_id)




search()
