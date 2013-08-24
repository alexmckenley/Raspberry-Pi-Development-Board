import twitter, time
from googlevoice import Voice
from googlevoice.util import input

voice = Voice()
voice.login(email="sobr.co", passwd="Iaamo1824")
print "Login Complete..."
print "getting tweets..."
api = twitter.Api()
s = api.GetUserTimeline("FunnySexFacts", count=10)

#phoneNumber = '6614928478'
phoneNumber = '8012100524'
#phoneNumber = ['4355312835','4355593425'] #Cameron + John


print "Sending Messages:"
i = 1

for x in s:
	try:
		voice.send_sms(phoneNumber, x.text)
	except Exception as inst:
		print type(inst)
		print inst
		continue
	if i == 1:
		print i, " message sent"
	else:
		print i, " messages sent"
	i += 1
	time.sleep(5)

print "Complete, logging out..."
voice.logout()
#print [x.text for x in s]
