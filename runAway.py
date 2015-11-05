# Test for movement in stright line


import pi2go, time

# Reading single character by forcing stdin to raw mode
import sys
import tty
import termios
import threading

# main loop
speed = 100
pi2go.init()

while True:
    print pi2go.getDistance()
    if pi2go.getDistance() <= 50:
        pi2go.reverse(speed);
        time.sleep(3)
        pi2go.stop()
    time.sleep(0.1)   

pi2go.cleanup()
    
