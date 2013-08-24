#This code is for use with the 74HC595 Line Driver IC

import RPi.GPIO as GPIO
import time

#Global variable to hold the outputs
registers = [False] * 8

###############    INIT   ###################
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)     #Data Pin
    GPIO.setup(17, GPIO.OUT)    #Serial Clock
    GPIO.setup(21, GPIO.OUT)    #Latch Clock


############### SET FUNCTION ###################
# Pass it registers array, and write the data to the pins.
def set(pin, value):
    global registers
    registers[pin] = value
    
    GPIO.output(21, False)
    
    for i in registers:
        GPIO.output(17, False)
        GPIO.output(4, i)
        GPIO.output(17, True)

    GPIO.output(21, True)
    

############### GET FUNCTION ################### 
# Return the value of registers at the index provided
def get(pin):
    global registers
    return registers[pin]

############### CLEAR ALL PINS ##################
# Turn all output pins off
def clear():
    global registers
    registers = [False] * 8
    set(0, False)


############### MAIN FUNCTION ###################
def main():
    setup()
    global registers
    
    for i in range(11):
        clear()
        print registers
        time.sleep(1)
        set(0, True)
        print registers
        time.sleep(1)
        set(7, True)
        print registers
        time.sleep(1)
    print get(7)
    print get(6)
        
    


if __name__ == '__main__':
  main()



    