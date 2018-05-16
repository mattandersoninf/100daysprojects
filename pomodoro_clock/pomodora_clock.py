#!python3

import datetime
from datetime import date, timedelta
import time

"""
Note: This could be done with the time class but the purpose of
writing it with the datetime class is just so you get used to using it.
expand on it and see if you can make a flask app, have fun!
"""

"""
This pomodoro function uses the timedelta function to store 25 minutes and then decrements it by seconds and returns the
resulting string until it hits 0 seconds and 0 minutes. The timdelta function doesn't have a minute attribute or strftime
function so I compensate for those just by using python str's format method with zero padding, some arithmetic and the seconds
attribute of the timedelta class. The total_seconds() method is preferred for larger time intervals but functions the same as the
seconds attribute.
"""

def p_clock_work():
	work_time = timedelta(minutes=25)
	while work_time != timedelta(seconds=0):
		work_time = work_time - timedelta(seconds=1)
		print('{:02d}:{:02d}'.format(int((work_time.total_seconds()-work_time.total_seconds()%60)/60), work_time.seconds%60))
		# this is so the chage in time is actually a second. Without it, the function would finish in a fraction of a second
		time.sleep(1)
	print("Take a brake. You've earned it.")

"""
insert future expansion for short break time and long break time functions and giving the main function the ability to call each individual
function from the command line
"""


if __name__ == '__main__':
	p_clock_work()