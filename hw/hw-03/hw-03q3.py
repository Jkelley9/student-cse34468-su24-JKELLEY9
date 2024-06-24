# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
pwmPin = 18 # Broadcom pin 18 (P1 pin 12)
RedLedPin = 23 # Broadcom pin 23 (P1 pin 16)
GreenLedPin = 21 # Broadcom pin 21
butPin = 17 # Broadcom pin 17 (P1 pin 11)

dc = 95 # duty cycle (0-100) for PWM pin

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(ledPin, GPIO.OUT) # LED pin set as output
GPIO.setup(pwmPin, GPIO.OUT) # PWM pin set as output
pwm = GPIO.PWM(pwmPin, 50)  # Initialize PWM on pwmPin 100Hz frequency
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

# Initial state for LEDs:
GPIO.output(ledPin, GPIO.LOW)
pwm.start(dc)

print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        if getDistance()<0.5: # Red turn on
            GPIO.output(RedLedPin, GPIO.HIGH)
            GPIO.output(GreenLedPin, GPIO.LOW)
        elif getDistance()>1.5: # Green LED turns on:
            GPIO.output(RedLedPin, GPIO.LOW)
            GPIO.output(GreenLedPin, GPIO.HIGH)
        else: # Off when not in range
            GPIO.output(RedLedPin, GPIO.LOW)
            GPIO.output(GreenLedPin, GPIO.LOW)
        time.sleep(0.075)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    pwm.stop() # stop PWM
    GPIO.cleanup() # cleanup all GPIO
