import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.output(4, False);
GPIO.output(17, False);
GPIO.output(21, True);
GPIO.output(22, True);


print "Press 'q' to quit"
while 1:
    
    
	nb = raw_input("Please Enter a Number:")
	if nb == 'q' or nb == 'Q':
		break
	try:
		nb = int(nb)
	except:
		print "Error, try again"
		continue
	if nb == 1:
		GPIO.output(22, True)
	elif nb == 0:
		GPIO.output(22, False)
	else:
		print "Number not recognized"
		continue
	
GPIO.cleanup()