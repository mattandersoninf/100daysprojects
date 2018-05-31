import itertools
import sys
import time
import random

lightcolors = itertools.cycle('green amber red'.split())

def trafficLight():
    # remember to add exit parameter
    for color in lightcolors:
        # stay on the same line while iterating through the traffic light colors
        # modified conditionals for colors
        if color == 'green':
            sys.stdout.write('\r' + 'Go!')
            # get rid of the previous iteration as you cycle through
            sys.stdout.flush()
            # delay the iterations by 1 second
            time.sleep(random.randint(3,7))
        elif color == 'amber':
            sys.stdout.write('\r' + 'Slow Down!')
            # get rid of the previous iteration as you cycle through
            sys.stdout.flush()
            # delay the iterations by 1 second
            time.sleep(random.randint(3,7))
        else:
            sys.stdout.write('\r' + 'Stop!')
            # get rid of the previous iteration as you cycle through
            sys.stdout.flush()
            # delay the iterations by 1 second
            time.sleep(random.randint(3,7))

if __name__ == '__main__':
    trafficLight()