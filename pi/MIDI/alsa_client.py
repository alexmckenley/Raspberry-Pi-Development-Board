import alsaseq, time, dev_board as pi

alsaseq.client( 'Python', 1, 0, False )
alsaseq.connectfrom( 0, 14, 0 )
alsaseq.start()

playChannels = [0 for x in range(16)]
pinChannels = [0,0,0,0]
pinNotes = [0,0,0,0]

def midi_process(ev):
  global pinNotes
  global pinChannels
  if (ev[0] == alsaseq.SND_SEQ_EVENT_PGMCHANGE):
    
    #clear pins state
    clearPinChannels()
    clearPinNotes()
    
    print "PGMCHANGE: channel ", ev[7][0], " ", ev[7][5]
    
    #filter out base, percussion, or synth
    if (ev[7][5] >= 8 and ev[7][5] <= 15) or (ev[7][5] >= 32 and ev[7][5] <= 39) or (ev[7][5] >= 88 and ev[7][5] <= 103):
      setPlayChannel(ev[7][0], 0)
    else:
      setPlayChannel(ev[7][0], 1)
    
    #if event is NOTEON(6) or NOTEOFF(7)
  elif (ev[0] == 6) or (ev[0] == 7):
    #print "GOT NOTE_X"
    if isPlayChannel(ev[7][0]):
      isOn = 1
      if (ev[0] == 7):
        isOn = 0
      
      noteMod = ev[7][1] % 12
      
      noteBin = noteMod / 3
      
      pinIndex = int(noteBin)
      
      if isOn:
        if (pinNotes[pinIndex] == -1) or (pinChannels[pinIndex] > ev[7][0]):
          
          if( (pinChannels[pinIndex] > ev[7][0] ) and (pinNotes[pinIndex] != -1)):
            print "OVERRIDING CHANNEL ", pinChannels[pinIndex], " for ", ev[7][0]

          
          pi.setRelay(pinIndex, 1)
          pi.setOutput(pinIndex, 1)
          pinNotes[pinIndex] = ev[7][1]
          pinChannels[pinIndex] = ev[7][0]
      else:
        if (pinNotes[pinIndex] == ev[7][1]) and (pinChannels[pinIndex] == ev[7][0]):
          pi.setRelay(pinIndex, 0)
          pi.setOutput(pinIndex, 0)
          pinNotes[pinIndex] = -1
          pinChannels[pinIndex] = 32767
    
  #unhandled event
  else:
    #print "unhandeled event: ", ev[1]
    pass

def clearPinChannels():
  global pinChannels
  pinChannels = [32767 for x in pinChannels]
  
def clearPinNotes():
  global pinNotes
  pinNotes = [-1 for x in pinNotes]
  
def setPlayChannel(channel, value):
  global playChannels
  if value == 0:
    print "dont play channel: ", channel
  playChannels[channel] = value
  
def isPlayChannel(channel):
  global playChannels
  if channel == 9:
    return 0
  else:
    return playChannels[channel]
    
def resetPlayChannels():
  global playChannels
  playChannels = [1 for x in playChannels]
  




#clear pins state
clearPinChannels()
clearPinNotes()
resetPlayChannels();

while 1:
  #print "inputs pending: ", alsaseq.inputpending()
  #if alsaseq.inputpending():
  #  event = alsaseq.input()
  #  print event
  if alsaseq.inputpending():
    event = alsaseq.input()
    #print event
    midi_process(event)
    
  
  
  