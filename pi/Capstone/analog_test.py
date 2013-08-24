import dev_board as pi
import time

def main():
  try:
    pi.pinMode('D', "1111")
    while 1:
      '''
      #value = pi.analogRead(0)
      for x in range(175):
        pi.analogWrite(0,x)
        time.sleep(.005)
      #pi.setRelay(0,1)
      for x in range(175,0,-1):
        pi.analogWrite(0,x)
        time.sleep(.005)
      #pi.setRelay(0,0)'''
      
      value = pi.analogRead(0)
      print value
      value = value / 70.0
      pi.setRelay(0,1)
      pi.digitalWrite(3,1)
      time.sleep(value)
      pi.setRelay(0,0)
      value = pi.analogRead(0)
      pi.digitalWrite(3,0)
      time.sleep(value/70.0)
    
    
  except KeyboardInterrupt:
    pi.cleanup()
    
  
def flash():
  for x in range(3):
    pi.setRelay(0,1)
    time.sleep(.25)
    pi.setRelay(0,0)
    time.sleep(.25)
  return

if __name__ == '__main__':
  main()