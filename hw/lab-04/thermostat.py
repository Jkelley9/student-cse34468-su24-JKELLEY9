# thermostat-start.py
#
# Name(s): Lewin Kelley
# E-mail(s): jkelley9@nd.edu
#

import time
from sense_hat import SenseHat
import mqtt_link as mqttnd
import json
# Your functions go here
def set_tens(number): # Used to create tens digit
  sense.set_pixel(0,2,(0,0,0))
  sense.set_pixel(0,3,(0,0,0))
  sense.set_pixel(0,4,(0,0,0))
  sense.set_pixel(0,5,(0,0,0))
  sense.set_pixel(0,6,(0,0,0))
  sense.set_pixel(1,2,(0,0,0))
  sense.set_pixel(1,3,(0,0,0))
  sense.set_pixel(1,4,(0,0,0))
  sense.set_pixel(1,5,(0,0,0))
  sense.set_pixel(1,6,(0,0,0))
  sense.set_pixel(2,2,(0,0,0))
  sense.set_pixel(2,3,(0,0,0))
  sense.set_pixel(2,4,(0,0,0))
  sense.set_pixel(2,5,(0,0,0))
  sense.set_pixel(2,6,(0,0,0))
  if number == 1:
    sense.set_pixel(2,2,(255,0,0))
    sense.set_pixel(2,3,(255,0,0))
    sense.set_pixel(2,4,(255,0,0))
    sense.set_pixel(2,5,(255,0,0))
    sense.set_pixel(2,6,(255,0,0))
  elif number ==2:
    sense.set_pixel(0,2,(255,0,0))
    sense.set_pixel(1,2,(255,0,0))
    sense.set_pixel(2,2,(255,0,0))
    sense.set_pixel(2,3,(255,0,0))
    sense.set_pixel(2,4,(255,0,0))
    sense.set_pixel(1,4,(255,0,0))
    sense.set_pixel(0,4,(255,0,0))
    sense.set_pixel(0,5,(255,0,0))
    sense.set_pixel(0,6,(255,0,0))
    sense.set_pixel(1,6,(255,0,0))
    sense.set_pixel(2,6,(255,0,0))
  elif number ==3:
    sense.set_pixel(0,2,(255,0,0))
    sense.set_pixel(1,2,(255,0,0))
    sense.set_pixel(2,2,(255,0,0))
    sense.set_pixel(2,3,(255,0,0))
    sense.set_pixel(2,4,(255,0,0))
    sense.set_pixel(2,5,(255,0,0))
    sense.set_pixel(2,6,(255,0,0))
    sense.set_pixel(1,4,(255,0,0))
    sense.set_pixel(0,6,(255,0,0))
    sense.set_pixel(1,6,(255,0,0))
    sense.set_pixel(2,6,(255,0,0))
  elif number ==4:
    sense.set_pixel(0,2,(255,0,0))
    sense.set_pixel(0,3,(255,0,0))
    sense.set_pixel(0,4,(255,0,0))
    sense.set_pixel(1,4,(255,0,0))
    sense.set_pixel(2,4,(255,0,0))
    sense.set_pixel(2,3,(255,0,0))
    sense.set_pixel(2,2,(255,0,0))
    sense.set_pixel(2,5,(255,0,0))
    sense.set_pixel(2,6,(255,0,0))
  elif number ==5:
    sense.set_pixel(0,2,(255,0,0))
    sense.set_pixel(1,2,(255,0,0))
    sense.set_pixel(2,2,(255,0,0))
    sense.set_pixel(0,3,(255,0,0))
    sense.set_pixel(0,4,(255,0,0))
    sense.set_pixel(1,4,(255,0,0))
    sense.set_pixel(2,4,(255,0,0))
    sense.set_pixel(2,5,(255,0,0))
    sense.set_pixel(2,6,(255,0,0))
    sense.set_pixel(1,6,(255,0,0))
    sense.set_pixel(0,6,(255,0,0))
  elif number ==6:
    sense.set_pixel(0,2,(255,0,0))
    sense.set_pixel(1,2,(255,0,0))
    sense.set_pixel(2,2,(255,0,0))
    sense.set_pixel(0,3,(255,0,0))
    sense.set_pixel(0,4,(255,0,0))
    sense.set_pixel(1,4,(255,0,0))
    sense.set_pixel(2,4,(255,0,0))
    sense.set_pixel(2,5,(255,0,0))
    sense.set_pixel(2,6,(255,0,0))
    sense.set_pixel(1,6,(255,0,0))
    sense.set_pixel(0,6,(255,0,0))
    sense.set_pixel(0,5,(255,0,0))
  elif number==7:
    sense.set_pixel(2,2,(255,0,0))
    sense.set_pixel(2,3,(255,0,0))
    sense.set_pixel(2,4,(255,0,0))
    sense.set_pixel(2,5,(255,0,0))
    sense.set_pixel(2,6,(255,0,0))
    sense.set_pixel(1,2,(255,0,0))
    sense.set_pixel(0,2,(255,0,0))
  elif number ==8:
    sense.set_pixel(0,2,(255,0,0))
    sense.set_pixel(1,2,(255,0,0))
    sense.set_pixel(2,2,(255,0,0))
    sense.set_pixel(0,3,(255,0,0))
    sense.set_pixel(0,4,(255,0,0))
    sense.set_pixel(1,4,(255,0,0))
    sense.set_pixel(2,4,(255,0,0))
    sense.set_pixel(2,5,(255,0,0))
    sense.set_pixel(2,6,(255,0,0))
    sense.set_pixel(1,6,(255,0,0))
    sense.set_pixel(0,6,(255,0,0))
    sense.set_pixel(0,5,(255,0,0))
    sense.set_pixel(2,3,(255,0,0))
  elif number ==9:
    sense.set_pixel(0,2,(255,0,0))
    sense.set_pixel(1,2,(255,0,0))
    sense.set_pixel(2,2,(255,0,0))
    sense.set_pixel(0,3,(255,0,0))
    sense.set_pixel(0,4,(255,0,0))
    sense.set_pixel(1,4,(255,0,0))
    sense.set_pixel(2,4,(255,0,0))
    sense.set_pixel(2,5,(255,0,0))
    sense.set_pixel(2,6,(255,0,0))
    sense.set_pixel(1,6,(255,0,0))
    sense.set_pixel(0,6,(255,0,0))
    sense.set_pixel(2,3,(255,0,0))
  elif number ==0:
    sense.set_pixel(2,2,(255,0,0))
    sense.set_pixel(2,3,(255,0,0))
    sense.set_pixel(2,4,(255,0,0))
    sense.set_pixel(2,5,(255,0,0))
    sense.set_pixel(2,6,(255,0,0))
    sense.set_pixel(0,2,(255,0,0))
    sense.set_pixel(0,3,(255,0,0))
    sense.set_pixel(0,4,(255,0,0))
    sense.set_pixel(0,5,(255,0,0))
    sense.set_pixel(0,6,(255,0,0))
    sense.set_pixel(1,6,(255,0,0))
    sense.set_pixel(1,2,(255,0,0))
    

def set_ones(number): # Sets ones digit of display
  sense.set_pixel(4,2,(0,0,0))
  sense.set_pixel(4,3,(0,0,0))
  sense.set_pixel(4,4,(0,0,0))
  sense.set_pixel(4,5,(0,0,0))
  sense.set_pixel(4,6,(0,0,0))
  sense.set_pixel(5,2,(0,0,0))
  sense.set_pixel(5,3,(0,0,0))
  sense.set_pixel(5,4,(0,0,0))
  sense.set_pixel(5,5,(0,0,0))
  sense.set_pixel(5,6,(0,0,0))
  sense.set_pixel(6,2,(0,0,0))
  sense.set_pixel(6,3,(0,0,0))
  sense.set_pixel(6,4,(0,0,0))
  sense.set_pixel(6,5,(0,0,0))
  sense.set_pixel(6,6,(0,0,0))
  if number == 1:
    sense.set_pixel(6,2,(255,0,0))
    sense.set_pixel(6,3,(255,0,0))
    sense.set_pixel(6,4,(255,0,0))
    sense.set_pixel(6,5,(255,0,0))
    sense.set_pixel(6,6,(255,0,0))
  elif number ==2:
    sense.set_pixel(4,2,(255,0,0))
    sense.set_pixel(5,2,(255,0,0))
    sense.set_pixel(6,2,(255,0,0))
    sense.set_pixel(6,3,(255,0,0))
    sense.set_pixel(6,4,(255,0,0))
    sense.set_pixel(5,4,(255,0,0))
    sense.set_pixel(4,4,(255,0,0))
    sense.set_pixel(4,5,(255,0,0))
    sense.set_pixel(4,6,(255,0,0))
    sense.set_pixel(5,6,(255,0,0))
    sense.set_pixel(6,6,(255,0,0))
  elif number ==3:
    sense.set_pixel(4,2,(255,0,0))
    sense.set_pixel(5,2,(255,0,0))
    sense.set_pixel(6,2,(255,0,0))
    sense.set_pixel(6,3,(255,0,0))
    sense.set_pixel(6,4,(255,0,0))
    sense.set_pixel(6,5,(255,0,0))
    sense.set_pixel(6,6,(255,0,0))
    sense.set_pixel(5,4,(255,0,0))
    sense.set_pixel(4,6,(255,0,0))
    sense.set_pixel(5,6,(255,0,0))
    sense.set_pixel(6,6,(255,0,0))
  elif number ==4:
    sense.set_pixel(4,2,(255,0,0))
    sense.set_pixel(4,3,(255,0,0))
    sense.set_pixel(4,4,(255,0,0))
    sense.set_pixel(5,4,(255,0,0))
    sense.set_pixel(6,4,(255,0,0))
    sense.set_pixel(6,3,(255,0,0))
    sense.set_pixel(6,2,(255,0,0))
    sense.set_pixel(6,5,(255,0,0))
    sense.set_pixel(6,6,(255,0,0))
  elif number ==5:
    sense.set_pixel(4,2,(255,0,0))
    sense.set_pixel(5,2,(255,0,0))
    sense.set_pixel(6,2,(255,0,0))
    sense.set_pixel(4,3,(255,0,0))
    sense.set_pixel(4,4,(255,0,0))
    sense.set_pixel(5,4,(255,0,0))
    sense.set_pixel(6,4,(255,0,0))
    sense.set_pixel(6,5,(255,0,0))
    sense.set_pixel(6,6,(255,0,0))
    sense.set_pixel(5,6,(255,0,0))
    sense.set_pixel(4,6,(255,0,0))
  elif number ==6:
    sense.set_pixel(4,2,(255,0,0))
    sense.set_pixel(5,2,(255,0,0))
    sense.set_pixel(6,2,(255,0,0))
    sense.set_pixel(4,3,(255,0,0))
    sense.set_pixel(4,4,(255,0,0))
    sense.set_pixel(5,4,(255,0,0))
    sense.set_pixel(6,4,(255,0,0))
    sense.set_pixel(6,5,(255,0,0))
    sense.set_pixel(6,6,(255,0,0))
    sense.set_pixel(5,6,(255,0,0))
    sense.set_pixel(4,6,(255,0,0))
    sense.set_pixel(4,5,(255,0,0))
  elif number==7:
    sense.set_pixel(6,2,(255,0,0))
    sense.set_pixel(6,3,(255,0,0))
    sense.set_pixel(6,4,(255,0,0))
    sense.set_pixel(6,5,(255,0,0))
    sense.set_pixel(6,6,(255,0,0))
    sense.set_pixel(5,2,(255,0,0))
    sense.set_pixel(4,2,(255,0,0))
  elif number ==8:
    sense.set_pixel(4,2,(255,0,0))
    sense.set_pixel(5,2,(255,0,0))
    sense.set_pixel(6,2,(255,0,0))
    sense.set_pixel(4,3,(255,0,0))
    sense.set_pixel(4,4,(255,0,0))
    sense.set_pixel(5,4,(255,0,0))
    sense.set_pixel(6,4,(255,0,0))
    sense.set_pixel(6,5,(255,0,0))
    sense.set_pixel(6,6,(255,0,0))
    sense.set_pixel(5,6,(255,0,0))
    sense.set_pixel(4,6,(255,0,0))
    sense.set_pixel(4,5,(255,0,0))
    sense.set_pixel(6,3,(255,0,0))
  elif number ==9:
    sense.set_pixel(4,2,(255,0,0))
    sense.set_pixel(5,2,(255,0,0))
    sense.set_pixel(6,2,(255,0,0))
    sense.set_pixel(4,3,(255,0,0))
    sense.set_pixel(4,4,(255,0,0))
    sense.set_pixel(5,4,(255,0,0))
    sense.set_pixel(6,4,(255,0,0))
    sense.set_pixel(6,5,(255,0,0))
    sense.set_pixel(6,6,(255,0,0))
    sense.set_pixel(5,6,(255,0,0))
    sense.set_pixel(4,6,(255,0,0))
    sense.set_pixel(6,3,(255,0,0))
  elif number ==0:
    sense.set_pixel(6,2,(255,0,0))
    sense.set_pixel(6,3,(255,0,0))
    sense.set_pixel(6,4,(255,0,0))
    sense.set_pixel(6,5,(255,0,0))
    sense.set_pixel(6,6,(255,0,0))
    sense.set_pixel(4,2,(255,0,0))
    sense.set_pixel(4,3,(255,0,0))
    sense.set_pixel(4,4,(255,0,0))
    sense.set_pixel(4,5,(255,0,0))
    sense.set_pixel(4,6,(255,0,0))
    sense.set_pixel(5,6,(255,0,0))
    sense.set_pixel(5,2,(255,0,0))
    
def flashing_num(): # Sets all number LEDs to Clear
  sense.set_pixel(4,2,(0,0,0))
  sense.set_pixel(4,3,(0,0,0))
  sense.set_pixel(4,4,(0,0,0))
  sense.set_pixel(4,5,(0,0,0))
  sense.set_pixel(4,6,(0,0,0))
  sense.set_pixel(5,2,(0,0,0))
  sense.set_pixel(5,3,(0,0,0))
  sense.set_pixel(5,4,(0,0,0))
  sense.set_pixel(5,5,(0,0,0))
  sense.set_pixel(5,6,(0,0,0))
  sense.set_pixel(6,2,(0,0,0))
  sense.set_pixel(6,3,(0,0,0))
  sense.set_pixel(6,4,(0,0,0))
  sense.set_pixel(6,5,(0,0,0))
  sense.set_pixel(6,6,(0,0,0))
  sense.set_pixel(0,2,(0,0,0))
  sense.set_pixel(0,3,(0,0,0))
  sense.set_pixel(0,4,(0,0,0))
  sense.set_pixel(0,5,(0,0,0))
  sense.set_pixel(0,6,(0,0,0))
  sense.set_pixel(1,2,(0,0,0))
  sense.set_pixel(1,3,(0,0,0))
  sense.set_pixel(1,4,(0,0,0))
  sense.set_pixel(1,5,(0,0,0))
  sense.set_pixel(1,6,(0,0,0))
  sense.set_pixel(2,2,(0,0,0))
  sense.set_pixel(2,3,(0,0,0))
  sense.set_pixel(2,4,(0,0,0))
  sense.set_pixel(2,5,(0,0,0))
  sense.set_pixel(2,6,(0,0,0))
  
def heating(value): # Turns on LEDs for heating depending on distance from set temp
  sense.set_pixel(1,0,(0,0,0))
  sense.set_pixel(3,0,(0,0,0))
  if value ==1:
    sense.set_pixel(0,0,(64,0,0))
    sense.set_pixel(3,0,(64,64,0))
  elif value ==2:
    sense.set_pixel(0,0,(111,0,0))
    sense.set_pixel(3,0,(111,111,0))
  elif value ==3:
    sense.set_pixel(0,0,(159,0,0))
    sense.set_pixel(3,0,(155,155,0))
  elif value ==4:
    sense.set_pixel(0,0,(206,0,0))
    sense.set_pixel(3,0,(206,206,0))
  else:
    sense.set_pixel(0,0,(255,0,0))
    sense.set_pixel(3,0,(255,255,0))

def cooling(value): # Turns on cooling LEDs depending on distance from set temp
  sense.set_pixel(0,0,(0,0,0))
  if value ==1:
    sense.set_pixel(1,0,(0,0,64))
    sense.set_pixel(3,0,(64,64,0))
  elif value ==2:
    sense.set_pixel(1,0,(0,0,111))
    sense.set_pixel(3,0,(111,111,0))
  elif value ==3:
    sense.set_pixel(1,0,(0,0,159))
    sense.set_pixel(3,0,(159,159,0))
  elif value ==4:
    sense.set_pixel(1,0,(0,0,206))
    sense.set_pixel(3,0,(206,206,0))
  else:
    sense.set_pixel(1,0,(0,0,255))
    sense.set_pixel(3,0,(255,255,0))
    
def noAC(): # Turns off heating/cooling LEDs
  sense.set_pixel(0,0,(0,0,0))
  sense.set_pixel(1,0,(0,0,0))
  sense.set_pixel(3,0,(0,0,0))


# The main body of the code

sense = SenseHat()

sense.clear()

LoopDelay = 0.5      # 250 ms per loop iteration

# Creating Variables
set_temp = 30 # Starting Set temp
setting_temp=1 # Loop for setting temp
type = "C"
loop = 1
temp = sense.get_temperature()
humidity = int(sense.get_humidity())
old_humidity = int(sense.get_humidity())
setting = "None"
# MQTT
theClient = mqttnd.connect_mqtt()
old_temp = int(sense.get_temperature())
old_set_temp = 26

while True:
  sense.set_pixel(7,0, (0,255,0))
    # Read the temperature
  if type =="C" and setting_temp==1:
    temp = int(sense.get_temperature())
    set_ones(temp%10)
    set_tens(temp%100//10)
  elif type == "F" and setting_temp==1:
    temp = int(sense.get_temperature()*9/5+32)
    set_ones(temp%10)
    set_tens(temp%100//10)
  # Convert to Fahrenheit and Celsius
  if type =="C" and loop ==0:
    set_temp = int((set_temp-32)*5/9)
    
  elif type =="F" and loop ==0:
    set_temp = int(set_temp*9/5+32)
  
  # Is the joystick doing anything?
  events = sense.stick.get_events()
  for event in events:
      # Skip releases
    if event.action == "pressed" and event.direction == "middle" and setting_temp ==1:
      setting_temp = 0
    elif event.action == "pressed" and event.direction == 'up' and setting_temp==0:
      set_temp+=1
      set_ones(set_temp%10)
      set_tens(set_temp%100//10)
    elif event.action == "pressed" and event.direction == 'down' and setting_temp==0:
      set_temp-=1
      set_ones(set_temp%10)
      set_tens(set_temp%100//10)
    elif event.action == "pressed" and event.direction == "middle" and setting_temp==0:
      setting_temp=1
      set_ones(temp%10)
      set_tens(temp%100//10)
    elif event.action == 'pressed' and event.direction =='left' and type =="F":
      type = "C"
      loop = -1
    elif event.action == 'pressed' and event.direction =='right' and type =="C":
      type = "F"
      loop = -1
  
  if setting_temp ==0 and type == "C": # Checking if setting and if Celcius
    flashing_num()
    time.sleep(0.5)
    set_ones(set_temp%10)
    set_tens(set_temp%100//10)
  elif setting_temp ==0 and type =="F":
    flashing_num()
    time.sleep(0.5)
    set_ones(set_temp%10)
    set_tens(set_temp%100//10)
  
  
  
    # Do we need to do anything in response to the temperature?
  
  if abs(temp-set_temp)>1:
    # Is it more than 1 degree away?
    #if temp-set_temp>1 or temp-set_temp<1:
    if temp-set_temp>0:
      cooling(abs(int(temp-set_temp))) # Turns on LED for cooling
      setting = "Cooling"
    elif temp-set_temp<0:
      heating(abs(int(temp-set_temp))) # Turns on LEDs for heating
      setting = "Heating"
  else:
    noAC() # If no heating/cooling needed
    setting = "N/A"
    # If it is more than 1 degree away, how far away is it?
  
  # Send Message if Change
  if temp != old_temp or set_temp != old_set_temp or humidity != old_humidity:
    if type =="C":
      the_data = {"Current Temp": str(temp), "Set Temp": str(set_temp), "Current Mode": setting, "Humidity": str(humidity)}
      theString = json.dumps(the_data)
    elif type =="F":
      the_data = {"Current Temp": str((temp-32)*5/9), "Set Temp": str((set_temp-32)*5/9), "Current Mode": setting, "Humidity": str(humidity)}
      theString = json.dumps(the_data)
    print("Sending Message")
    mqttnd.send_mqtt(theClient, "cse34468-su24/jkelley9/lab-04/info/", theString)
    old_temp = temp
    set_temp = old_set_temp
    humidity = old_humidity
  else:
    old_temp = temp
    set_temp = old_set_temp
    humidity = old_humidity

  time.sleep(LoopDelay)
  loop+=1
sense.set_pixel(7,0,(0,255,0))






