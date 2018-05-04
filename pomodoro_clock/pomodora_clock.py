#!python3

from datetime import datetime
from datetime import date
from datetime import timedelta
"""
note: this could be done with the time class but the purpose of
writing it with the datetime class is just so you get used to using it
refer to https://gist.github.com/jsonstackHouse/a34ab0f0ee918aeea8ee79be48bbf75d
expand on it and see if you can make a flask app, have fun!
"""

# activate the timer for working (25 min)
def pomodoro_clock_work():
	# get the start time
	start = datetime.today()
	# set the change in change
	working = timedelta(minutes=25)
	# get end time
	stop_working = start + working
	# let the user know when they should stop working
	print("The timer will end at:" + str(stop_working))
	# update displayed time every minute
	while datetime.today().minute() != stop_working.minute():
		print((datetime.today()))
		pass

# activate the timer for a short break (5 min)
def pomodoro_clock_short_break():

# activate the timer for a long break (30 min)
def pomodoro_clock_long_break():
