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

try:
    while True:
        if (pi2go.irLeftLine() == False):
            pi2go.go(speed * 0.94, speed)
        elif (pi2go.irLeftLine() == True):
            pi2go.spinleft(speed)   
        #if (pi2go.irLeftLine() == True and pi2go.irRightLine() == True):
        #    pi2go.go(speed * 0.94, speed)
        #elif (pi2go.irLeftLine() == False):
        #    pi2go.spinLeft(speed)
        #elif (pi2go.irRightLine() == False):
        #    pi2go.spinRight(speed)
        #elif (pi2go.irLeftLine() == False and pi2go.irRightLine() == False):
        #    pi2go.stop()
        #print(pi2go.irLeftLine())
        #print(pi2go.irRightLine())
        #print('#######')
        #time.sleep(3)
            
finally:
    pi2go.cleanup()
    
