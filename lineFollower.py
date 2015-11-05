# Test for movement in stright line


import pi2go, time

# Reading single character by forcing stdin to raw mode
import sys
import tty
import termios
import threading

# main loop
speed = 10
pi2go.init()
pi2go.go(speed * 0.94, speed)

try:
    while True:
        if (pi2go.irLeftLine()):
            print "Left"
        elif (pi2go.irRightLine()):
            print "Right"
finally:
    pi2go.cleanup()
    
