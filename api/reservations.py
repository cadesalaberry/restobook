# Because eve is not made to modify code programatically
# (see filters http://python-eve.org/config.html)
# Here is a sample using a list of reservations and restaurants


from datetime import datetime
from mock import reservations, restaurants


def get_all_reservations_from_restaurant(restaurant_id='23', reservations=reservations):

  result = [r for r in reservations if r['restaurant_id'] == restaurant_id]

  return result

def get_all_reservations_from_day(day="2015-01-01 03:55", reservations=reservations):
  
  def date(string):
    t = datetime.strptime(string, '%Y-%m-%d %H:%M')
    return t.date()

  result = [r for r in reservations if date(r['from']) == date(day)]

  return result


def get_headcount_from_reservations(reservations=reservations):

  headcount_list = [int(r['headcount']) for r in reservations]

  return sum(headcount_list)


"""
Query looks like:
date=2015-01-01&time=03%3A55&headcount=3
"""
def search(date='2015-01-01', time='03:55', headcount=3, restaurant_id="23"):

  dtime = date + ' ' + time

  desired_time = datetime.strptime(dtime, '%Y-%m-%d %H:%M')

  print desired_time

  res = get_all_reservations_from_restaurant(restaurant_id)

  print 'res\t', res

  day = get_all_reservations_from_day("2005-06-01 03:55")

  print 'day\t', day

  cnt = get_headcount_from_reservations(day)

  print 'cnt\t', cnt

  def would_reach_capacity(restaurant, currentcount, headcount):
    return int(restaurant['capacity']) - currentcount - headcount > 0

  unavailable = [r['id'] for r in restaurants if not would_reach_capacity(r, cnt, headcount)]

  print 'unavail\t', unavailable

  return [r for r in restaurants if r['id'] not in unavailable]



print search()
