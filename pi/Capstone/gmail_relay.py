#Alex Taylor
#Python Gmail Notifier
#Southern Utah University, 2013


#import required libraries
import dev_board as pi, feedparser, time
 
#provide gmail login credentials 
USERNAME = "username_here"     # just the part before the @ sign
PASSWORD = "password_here"     
 
NEWMAIL_OFFSET = 0        # how many messages to keep the light off
MAIL_CHECK_FREQ = 60      # check mail every 60 seconds
 

RELAY_NUM = 0


try:
  #loop forever
  while True:
   
    #fetch number of unread messages using feedparser 
    newmails = int(feedparser.parse("https://" + USERNAME + ":" + PASSWORD +"@mail.google.com/gmail/feed/atom")["feed"]["fullcount"])
    print newmails
   
    #compare number of new emails to the offset
    #if newmails is greater than offset, turn lamp on, else turn lamp off
    if newmails > NEWMAIL_OFFSET:
      pi.setRelay(RELAY_NUM, 1)
    else:
      pi.setRelay(RELAY_NUM, 0)

    #notify the user every time the program checks gmail
    print "Just Updated..."
    
    #time delay to check Gmail
    time.sleep(MAIL_CHECK_FREQ)
    
except KeyboardInterrupt:
  pi.cleanup();