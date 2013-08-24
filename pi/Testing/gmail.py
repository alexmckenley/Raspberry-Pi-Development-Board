import RPi.GPIO as GPIO, feedparser, time
 
DEBUG = 1
 
USERNAME = "alexmckenley"     # just the part before the @ sign, add yours here
PASSWORD = "lrtp&zfPa=P2G"     
 
NEWMAIL_OFFSET = 0        # my unread messages never goes to zero, yours might
MAIL_CHECK_FREQ = 60      # check mail every 60 seconds
 
GPIO.setmode(GPIO.BCM)
GREEN_LED = 17
#RED_LED = 23
GPIO.setup(GREEN_LED, GPIO.OUT)
#GPIO.setup(RED_LED, GPIO.OUT)
 
while True:
 
        newmails = int(feedparser.parse("https://" + USERNAME + ":" + PASSWORD +"@mail.google.com/gmail/feed/atom")["feed"]["fullcount"])
#	newmails = 5
	print newmails
	if DEBUG:
                print "You have", newmails, "new emails!"
 
        if newmails > NEWMAIL_OFFSET:
                GPIO.output(GREEN_LED, True)
#                GPIO.output(RED_LED, False)
        else:
                GPIO.output(GREEN_LED, False)
 #               GPIO.output(RED_LED, True)
 		print "Just Updated..."
        time.sleep(MAIL_CHECK_FREQ)