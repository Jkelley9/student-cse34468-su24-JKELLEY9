import math

def calculateSpeed(current, old):
    radius = 9.5
    circumference = math.pi*radius*2
    counts = current-old
    distance_travelled = counts*circumference/2 # Distance in inches
    speed = distance_travelled/0.1 # Speed in inches per second
    speed = speed*3600/(5280*12) # Speed in MPH
    return speed