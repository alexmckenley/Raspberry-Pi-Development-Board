#This code is for use with the 74HC595 Line Driver IC

import RPi.GPIO as GPIO
import time

###############    INIT   ###################
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)     #Data Pin
    GPIO.setup(17, GPIO.OUT)    #Serial Clock
    GPIO.setup(21, GPIO.OUT)    #Latch Clock

############### WRITE FUNCTION ###################
# Pass it registers array, and write the data to the pins.
def write(z):  
    GPIO.output(21, False)
    
    for i in z:
        GPIO.ouput(17, False)
        if i == 0:
            GPIO.output(4, False)
        else:
            GPIO.output(4, True)
        GPIO.output(17, True)
    
    GPIO.output(21, True)

############### CLEAR ALL PINS ##################
# Sets the register array to all zeroes
def clear():
    return [0] * 8


############### MAIN FUNCTION ###################
def main():
    setup()
    for w in range(11):
        registers = clear()
        write(registers)
        print "Printing: ", registers
    
        time.sleep(1)
    
        registers = [1] * 8
        write(registers)
        print "Printing: ", registers
    
        time.sleep(1)
        
    GPIO.cleanup()


if __name__ == '__main__':
  main()



    