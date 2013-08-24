#Alex Taylor
#Twitter Notifier
#Southern Utah University, 2013

#import required libraries
import dev_board as pi, time, twitter

#access the twitter API using my oauth token
def main():
  api = twitter.Api(consumer_key='EGJDu5LfotURQkzkduAleA',consumer_secret='PaAnVZZmTu0sHDebUSHm0smJU14Ue9t17ZN7fEHSgus',
  access_token_key='1392430634-BitdX4NV4WAtCSib1c5zAzV0Gp3CpzzSmHLve3T', access_token_secret='VXMDx24kJxH3Ek11A92aiAhUHf7xoLIgaBPB5nvCk')

  
  
  try:
    #flash lamp to signal program start
    flash(1)
    
    #check twitter initially to determine most current id number
    query = api.GetSearch(term='#SUUEET')
    idNum = 0
    for s in query:
      if idNum < s.id:
        idNum = s.id

    #loop forever
    while 1:
      count = 0
      #query twitter using specific string
      query = api.GetSearch(term='#SUUEET', since_id=idNum)
      print "Just Checked"
      #determine how mnay new results have been returned
      for s in query:
        #print each result on the screen
        print s.text
        idNum = s.id
        count += 1
        #flash the lamp for each result
        flash(count)
      #limit the rate we poll twitter
      time.sleep(60)

  except KeyboardInterrupt:
    pi.cleanup()
    
#function to flash the lamp 'count' number of times
def flash(count):
  for x in range(count):
    for y in range(3):
      pi.setRelay(0,1)
      time.sleep(.25)
      pi.setRelay(0,0)
      time.sleep(.25)
    time.sleep(1)
  return

if __name__ == '__main__':
  main()
