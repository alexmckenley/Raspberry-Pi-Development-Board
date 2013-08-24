import RPi.GPIO as GPIO, time
from datetime import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

def clear():
	GPIO.output(4, False)
	GPIO.output(17, False)
	GPIO.output(21, False)
	GPIO.output(22, False)
	GPIO.output(8, False)
	GPIO.output(7, False)
	GPIO.output(25, False)
	GPIO.output(24, False)
 
def dec_to_bin(x):
	return str(int(bin(x)[2:]))

def output1(z):
	string = dec_to_bin(z)
	string = string.zfill(4)
	if int(string[-1]) == 0:
		GPIO.output(8, False)
	else:
		GPIO.output(8, True)
	if int(string[-2]) == 0:
		GPIO.output(7, False)
	else:
		GPIO.output(7, True)
	if int(string[-3]) == 0:
		GPIO.output(25, False)
	else:
		GPIO.output(25, True)
	if int(string[-4]) == 0:
		GPIO.output(24, False)
	else:
		GPIO.output(24, True)
	
def output2(z):
	string = dec_to_bin(z)
	string = string.zfill(4)
	if int(string[-1]) == 0:
		GPIO.output(4, False)
	else:
		GPIO.output(4, True)
	if int(string[-2]) == 0:
		GPIO.output(17, False)
	else:
		GPIO.output(17, True)
	if int(string[-3]) == 0:
		GPIO.output(21, False)
	else:
		GPIO.output(21, True)
	if int(string[-4]) == 0:
		GPIO.output(22, False)
	else:
		GPIO.output(22, True)


#BEGIN CODE
############################################################
clear()
cur = 0

for x in range(10):
	now = datetime.now()
	output1(now.second)
	output2(now.minute)
	print now.hour, now.minute, now.second
	time.sleep(1) 

#for i in range(33):
#	output(i)
#	time.sleep(.5)

"""
for y in range(5):
	clear()
	time.sleep(.1)
	print "Round ", y
	for x in range(0,4):
		if x == 0:
			GPIO.output(4, True)
			#print "Pin 4 is ON"
		elif x == 1:
			GPIO.output(17, True)
			#print "Pin 17 is ON"
		elif x == 2:
			GPIO.output(21, True)
			#print "Pin 21 is ON"
		elif x == 3:
			GPIO.output(22, True)
			#print "Pin 22 is ON"
		
		time.sleep(.1)
"""		
		
GPIO.cleanup()
