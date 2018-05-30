import itertools
import sys
import time

lightcolors = itertools.cycle(['green','amber','red'])

def trafficLight():
    # remember to add exit parameter
    while True:
        # stay on the same line while iterating through the traffic light colors
        sys.stdout.write('\r' + next(lightcolors))
        # get rid of the previous iteration as you cycle through
        sys.stdout.flush()
        # delay the iterations by 1 second
        time.sleep(1)
        # to break loop, just type anything
        if input() != None: break

if __name__ == '__main__':
    trafficLight()