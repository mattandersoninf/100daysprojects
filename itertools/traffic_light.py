import itertools
import sys
import time

lightcolors = itertools.cycle(['green','amber','red'])

def trafficLight():
    while True:
        sys.stdout.write('\r' + next(lightcolors))
        sys.stdout.flush()
        time.sleep(0.5)


if __name__ == '__main__':
    trafficLight()