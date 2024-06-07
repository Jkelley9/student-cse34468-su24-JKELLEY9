# stoplight-us.py : Example code for a stoplight for a N-S US style stoplight
#
# Name(s):
# E-mail(s):
#

import time 
from sense_hat import SenseHat

# Your functions go here

# Set the stoplight to a specific setting
#   theHAT - the SenseHat object
#   theSetting - the setting to set the stoplight to
#     which is either red, yellow, or green
def setStoplightNS (theHAT, theSetting):
    if theSetting == 'Red':
        # Turn the red light on
        sense.set_pixel(2, 5, (255, 0, 0)) 
        # Turn off the yellow and green lights       
        sense.set_pixel(2, 6, (0, 0, 0))
        sense.set_pixel(2, 7, (0, 0, 0))
        
        # Turn off Walking
        sense.set_pixel(0,1,(0,0,0))
        sense.set_pixel(0,4,(0,0,0))
        sense.set_pixel(0,7,(0,0,0))
        # Red Lights
        sense.set_pixel(0,0,(255,0,0))
        sense.set_pixel(0,3,(255,0,0))
        sense.set_pixel(0,6,(255,0,0))
        
    elif theSetting == 'Yellow':
        # Turn the yellow light on
        sense.set_pixel(2, 6, (255, 255, 0))
        # Turn off the red and green lights       
        sense.set_pixel(2, 5, (0, 0, 0)) 
        sense.set_pixel(2, 7, (0, 0, 0))
        # Turn off Walking
        sense.set_pixel(0,1,(0,0,0))
        sense.set_pixel(0,4,(0,0,0))
        sense.set_pixel(0,7,(0,0,0))
        # Red Lights
        sense.set_pixel(0,0,(255,0,0))
        sense.set_pixel(0,3,(255,0,0))
        sense.set_pixel(0,6,(255,0,0))
    elif theSetting == 'Green':
        # Turn the green light on
        sense.set_pixel(2, 7, (0, 255, 0))
        # Turn off the red and yellow lights       
        sense.set_pixel(2, 5, (0, 0, 0)) 
        sense.set_pixel(2, 6, (0, 0, 0))
        #Walking
        sense.set_pixel(0,1,(0,255,0))
        sense.set_pixel(0,4,(0,255,0))
        sense.set_pixel(0,7,(0,255,0))
        # Red Lights
        sense.set_pixel(0,0,(0,0,0))
        sense.set_pixel(0,3,(0,0,0))
        sense.set_pixel(0,6,(0,0,0))
    elif theSetting == 'Yellow-Red':
        sense.set_pixel(2,5,(255,0,0))
        sense.set_pixel(2,6,(255,255,0))
        sense.set_pixel(2,7,(0,0,0))
        # Turn off Walking
        sense.set_pixel(0,1,(0,0,0))
        sense.set_pixel(0,4,(0,0,0))
        sense.set_pixel(0,7,(0,0,0))
        # Red Lights
        sense.set_pixel(0,0,(255,0,0))
        sense.set_pixel(0,3,(255,0,0))
        sense.set_pixel(0,6,(255,0,0))
def setStoplightEW (theHAT, theSetting):
    if theSetting == 'Red':
        # Turn the red light on
        sense.set_pixel(5, 2, (255, 0, 0)) 
        # Turn off the yellow and green lights       
        sense.set_pixel(6, 2, (0, 0, 0))
        sense.set_pixel(7, 2, (0, 0, 0))
        # Turn of Walking
        sense.set_pixel(6,0,(255,0,0))
        sense.set_pixel(7,0,(0,0,0))
    elif theSetting == 'Yellow':
        # Turn the yellow light on
        sense.set_pixel(6, 2, (255, 255, 0))
        # Turn off the red and green lights       
        sense.set_pixel(5, 2, (0, 0, 0)) 
        sense.set_pixel(7, 2, (0, 0, 0))
        # Turn of Walking
        sense.set_pixel(6,0,(255,0,0))
        sense.set_pixel(7,0,(0,0,0))
    elif theSetting == 'Green':
        # Turn the green light on
        sense.set_pixel(7, 2, (0, 255, 0))
        # Turn off the red and yellow lights       
        sense.set_pixel(5, 2, (0, 0, 0)) 
        sense.set_pixel(6, 2, (0, 0, 0))
        # Allow Walking
        # Turn of Walking
        sense.set_pixel(6,0,(0,0,0))
        sense.set_pixel(7,0,(0,255,0))
    elif theSetting == 'Yellow-Red':
        sense.set_pixel(5,2,(255,0,0))
        sense.set_pixel(6,2,(255,255,0))
        sense.set_pixel(7,2,(0,0,0))
        

##################################################
# Main Code is Here

sense = SenseHat()

LoopDelay = 0.25      # 250 ms per loop iteration
PreScalar = 10.00      # Set this higher to speed up for testing purposes
# PreScalar = 1.0

# Compute how long to wait on each loop
LoopDelay = LoopDelay / PreScalar

# Define each of the states
#
# Start at Red, go to Green, then Yellow, then back to Red
#
# State         Means What                   Next State      Ticks
# 
# Light-Red     Stay red for 35 seconds      Light-Green     35*4
# Light-Green   Stay green for 30 seconds    Light-Yellow    30*4
# Light-Yellow  Stay yellow for 5 seconds    Light-Red        5*4


TheState = 1
TicksToWait = 25 * 4

while True:
    # Decrease the counter - when we get to zero, we change
    TicksToWait -= 1

    if TheState == 1:
        # Set the stoplight to red
        setStoplightNS(sense, 'Red')
        setStoplightEW(sense,'Green')
    elif TheState == 2:
        # Set the stoplight to yellow
        setStoplightNS(sense, 'Red')
        setStoplightEW(sense,'Yellow')
        
    elif TheState == 3:
        setStoplightEW(sense,'Red')
        setStoplightNS(sense, 'Red')
    elif TheState == 4:
        setStoplightEW(sense,'Red')
        setStoplightNS(sense, 'Yellow-Red')
    elif TheState == 5:
        setStoplightEW(sense,'Red')
        setStoplightNS(sense, 'Green')
    elif TheState == 6:
        setStoplightEW(sense,'Red')
        setStoplightNS(sense, 'Yellow')
    elif TheState == 7:
        setStoplightEW(sense,'Red')
        setStoplightNS(sense, 'Red')
    elif TheState == 8:
        setStoplightEW(sense,'Yellow-Red')
        setStoplightNS(sense, 'Red')

    # Should we transition?
    if TicksToWait == 0:
        # Yes - but what to?

        if TheState == 1:
            TheState = 2
            TicksToWait = 5 * 4
        elif TheState == 2:
            TheState = 3
            TicksToWait = 5 * 4
        elif TheState == 3:
            TheState = 4
            TicksToWait = 5 * 4
        elif TheState == 4:
            TheState = 5
            TicksToWait = 25 * 4
        elif TheState ==5:
            TheState = 6
            TicksToWait = 5 * 4
        elif TheState == 6:
            TheState = 7
            TicksToWait = 5 * 4
        elif TheState == 7:
            TheState = 8
            TicksToWait = 5 * 4
        elif TheState == 8:
            TheState = 1
            TicksToWait = 25 * 4





    # All done - sleep and keep counting

    # Leave this code here
    time.sleep(LoopDelay)