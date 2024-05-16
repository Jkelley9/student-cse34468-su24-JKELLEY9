# mod-sense.py 
# 
# Adapted from the base code at https://trinket.io/sense-hat

from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def logo_n():
    G = green
    Y = yellow
    B = blue
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    B, B, O, O, O, O, O, B,
    B, O, B, O, O, O, O, B,
    B, O, O, B, O, O, O, B,
    B, O, O, O, B, O, O, B,
    B, O, O, O, O, B, O, B,
    B, O, O, O, O, O, B, B,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def logo_d():
    G = green
    Y = yellow
    B = blue
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    Y, Y, Y, O, O, O, O, O,
    Y, O, O, Y, Y, O, O, O,
    Y, O, O, O, Y, Y, O, O,
    Y, O, O, O, O, O, Y, O,
    Y, O, O, O, O, Y, O, O,
    Y, O, O, O, Y, Y, O, O,
    Y, Y, Y, Y, O, O, O, O,
    ]
    return logo

def logo_none():
    G = green
    Y = yellow
    B = blue
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

images = [logo_n, logo_d, logo_none]
count = 0

while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1
