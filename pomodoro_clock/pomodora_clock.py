#!python3

from datetime import timedelta
import time

"""
Note: This could be done with the time class but the purpose of
writing it with the datetime class is just so you get used to using it.
expand on it and see if you can make a flask app, have fun!
"""

"""
This pomodoro function uses the timedelta function to store 25 minutes and 
then decrements it by seconds and returns the resulting string until it hits 0 
seconds and 0 minutes. The timedelta function doesn't have a minute attribute 
or strftime function so I compensate for those just by using python string's 
format method with zero padding, some arithmetic and the seconds attribute of 
the timedelta class. The total_seconds() method is preferred for larger time 
intervals but functions the same as the seconds attribute.

TBH, this really doesn't need test functions. If you want to make some, go 
right ahead.
"""


# pomodoro timer for 25 minutes
def pomodoro_clock_work():
    work_time = timedelta(minutes=25)

    # just print the start time for the sake of OCD
    print('25:00')

    while work_time != timedelta(seconds=0):
        work_time = work_time - timedelta(seconds=1)

        print('{:02d}:{:02d}'.format(
            int((work_time.total_seconds() - work_time.total_seconds() % 60) / 60),
            work_time.seconds % 60))

        # this is so the change in time is actually a second. Without it, the
        #  function would finish in a fraction of a second
        time.sleep(1)

    print("Take a brake. You've earned it.")


# short 5 minute break
def pomodoro_clock_short():
    work_time = timedelta(minutes=5)

    # just print the start time for the sake of OCD
    print('05:00')

    while work_time != timedelta(seconds=0):
        work_time = work_time - timedelta(seconds=1)

        print('{:02d}:{:02d}'.format(
            int((work_time.total_seconds() - work_time.total_seconds() % 60) / 60), work_time.seconds % 60))

        # this is so the change in time is actually a second. Without it, the function would finish in a fraction of a
        #  second
        time.sleep(1)

    print("Take a brake. You've earned it.")


# long 30 minute break
def pomodoro_clock_long():
    work_time = timedelta(minutes=30)

    # just print the start time for the sake of OCD
    print('30:00')

    while work_time != timedelta(seconds=0):
        work_time = work_time - timedelta(seconds=1)

        print('{:02d}:{:02d}'.format(
            int((work_time.total_seconds() - work_time.total_seconds() % 60) / 60),
            work_time.seconds % 60))

        # this is so the change in time is actually a second. Without it, the
        #  function would finish in a fraction of a second
        time.sleep(1)

    print("Take a brake. You've earned it.")


if __name__ == '__main__':

    while True:

        cmd = input('Do you want to [w]ork, take a [s]hort break, take a [l]ong break, or close out?')

        if cmd == 'w':
            pomodoro_clock_work()
        elif cmd == 's':
            pomodoro_clock_short()
        elif cmd == 'l':
            pomodoro_clock_long()
        else:
            break
