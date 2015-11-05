# Test for movement in stright line


import pi2go, time

# Reading single character by forcing stdin to raw mode
import sys
import tty
import termios
import threading



#read distance in thread
running = True
def read_distance():
    global running
    while running:
        print pi2go.getDistance()
        if pi2go.getDistance() <= 10:
            pi2go.reverse(speed);
            time.sleep(3)
            pi2go.stop()
        time.sleep(0.25)





# main loop
speed = 100
pi2go.init()
thread = threading.Thread(target = read_distance)
thread.start()
    

finally:
    running = False
    time.sleep(0.25)
    pi2go.cleanup()
    
