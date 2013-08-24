#Alex Taylor
#Raspberry Pi Development Board
#Southern Utah University, 2013


import RPi.GPIO as GPIO
import time, serial, struct


#Initalize serial port
port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=0)

#Declare constants
OUTPUT = 1
INPUT = 0
relayPins = [4, 17, 21 ,22]
outputs = [23, 18, 25, 24]

#initalize GPIO output pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
for x in range(4):
  GPIO.setup(relayPins[x], GPIO.OUT)
  GPIO.setup(outputs[x], GPIO.OUT)
  GPIO.output(relayPins[x], 1)
  GPIO.output(outputs[x], 0)
  



#Turn the specified relay coil to the provided state
def setRelay(relayNum, state):
  GPIO.output(relayPins[relayNum], not state) # invert state because the relay is active low.
  
  
  
#Sets the specified extrenal output pin to the provided state
def setOutput(outputNum, state):
  GPIO.output(outputs[outputNum], state)



#Set the microcontroller pins to input or output

#args:
#ad = single character 'A' or 'D'
#pins = string with 4 1's or 0's

#Example: setMode('D', "1111") -- Sets all digital to outputs.
def pinMode(ad, pins):
  #Set the program flag true, and insert second bit(its irrevelant for setMode)
  temp = "11"
  #Determine if A or D channel
  if (ad == 'A'):
    #set a/d channel false if analog
    temp += "01"
    for x in range(4):
        temp += pins[x]
  elif (ad == 'D'):
    #set a/d channel true if digital
    temp += "11"
    for x in range(4):
        temp += pins[x]
  else:
    print "Error, Please choose A or D"
    return
  
  #convert the string of 1's and 0's to an integer
  temp = int(temp, 2)
  #Debugging - Uncomment to verify what integer value is being sent
  #print temp
  temp = struct.pack('B', temp)  # here you are packing the number 1 as a binary.
  port.write(temp)
  #wait until there is a response
  while (port.inWaiting() < 1):
    pass
  response = port.read(1)
  response = ord(response)
  if (response != 255):
    print "ERROR, didnt recieve a confirmation byte or its not equal to 255"
  
  

#set output pin over serial
def digitalWrite(pin, state):
  temp = "01"
  #set digital/analog bit depending on the value of pin
  if (pin < 4):
    temp += "10"
  else:
    temp += "00"
    pin -= 4
  
  for x in range(4):
    if (x == pin):
      temp += "1"
    else:
      temp += "0"
      
  #convert the string of 1's and 0's to an integer
  temp = int(temp, 2)
  #DEBUG
  #print(temp)
  temp = struct.pack('B', temp)  # pack the string to binary
  port.write(temp)
  #Send second byte containing the value
  port.write(struct.pack('B', state))

  #wait until there is a response
  while (port.inWaiting() < 1):
    pass
  response = port.read(1)
  response = ord(response)
  if (response != 255):
    print "ERROR, didnt recieve a confirmation byte or its not equal to 255", response
  
  
  
#Read a digital input pin over serial
def digitalRead(pin):
  temp = "0011"
  for x in range(4):
    if (x == pin):
      temp += "1"
    else:
      temp += "0"
  
  return read2(temp)
  

def analogRead(pin):
  temp = "0000"
  for x in range(4):
    if (x == pin):
      temp += "1"
    else:
      temp += "0"
      
  return read2(temp)
  
def read2(temp):
  #Clear out serial buffer
  port.read()
  #convert the string of 1's and 0's to an integer
  temp = int(temp, 2)
  #DEBUG
  #print(temp)
  temp = struct.pack('B', temp)  # pack the string to binary
  port.write(temp)
  while (port.inWaiting() < 1):
    pass
  response = port.read(1)
  return ord(response)


def analogWrite(pin, value):
  temp = "01"
  #set digital/analog bit depending on the value of pin
  temp += "11"
  
  for x in range(4):
    if (x == pin):
      temp += "1"
    else:
      temp += "0"
      
  #convert the string of 1's and 0's to an integer
  temp = int(temp, 2)
  #DEBUG
  #print(temp)
  temp = struct.pack('B', temp)  # pack the string to binary
  port.write(temp)
  #Send second byte containing the value
  port.write(struct.pack('B', value))

  #wait until there is a response
  while (port.inWaiting() < 1):
    pass
  response = port.read(1)
  response = ord(response)
  if (response != 255):
    print "ERROR, didnt recieve a confirmation byte or its not equal to 255", response      
      
      

def cleanup():
  for x in range(4):
    GPIO.output(relayPins[x], 1)
    GPIO.output(outputs[x], 0)
  
  pinMode('D', "0000");
  pinMode('A', "0000");
