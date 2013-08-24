#include <alsa/asoundlib.h>
#include <wiringPi.h>
#include <limits.h>
#include <unistd.h>
static snd_seq_t *seq_handle;
static int in_port;
static int pinMap[] = {23, 18, 25, 24};
static int pinMap2[] = {4, 17, 21 ,22};

#define THRUPORTCLIENT 14
#define THRUPORTPORT 0
#define MY_NUM_PINS 4

void midi_open(void)
{
    snd_seq_open(&seq_handle, "default", SND_SEQ_OPEN_INPUT, 0);

    snd_seq_set_client_name(seq_handle, "LightOrgan");
    in_port = snd_seq_create_simple_port(seq_handle, "listen:in",
                      SND_SEQ_PORT_CAP_WRITE|SND_SEQ_PORT_CAP_SUBS_WRITE,
                      SND_SEQ_PORT_TYPE_APPLICATION);
 
    if( snd_seq_connect_from(seq_handle, in_port, THRUPORTCLIENT, THRUPORTPORT) == -1) {
       perror("Can't connect to thru port");
       exit(-1);
    } 

}


snd_seq_event_t *midi_read(void)
{
    snd_seq_event_t *ev = NULL;
    snd_seq_event_input(seq_handle, &ev);
    return ev;
}


//Currently playing note, by pin
int pinNotes[MY_NUM_PINS];

//Currently playing channel, by pin
int pinChannels[MY_NUM_PINS];

//Enabled channels
int playChannels[16];


void clearPinNotes() {
   int i;
   for(i=0; i<MY_NUM_PINS; i++) {
      pinNotes[i] = -1;
   }
}

void clearPinChannels() {
   int i;
   for(i=0; i<MY_NUM_PINS; i++) {
      pinChannels[i] = INT_MAX;
   }
}

void clearPinsState() {
  clearPinNotes();
  clearPinChannels();
}

void pinsOn() {
   int i;
   for(i=0; i<MY_NUM_PINS; i++) {
      digitalWrite(i, 1); 
   }
}

void pinsOff() {
   int i;
   for(i=0; i<MY_NUM_PINS; i++) {
      digitalWrite(i, 1); 
   }
}


void setPlayChannel(int channel, int val) {
  if(val == 0) printf("dont play channel : %2d\n", channel);
  playChannels[channel] = val;  
}

int isPlayChannel(int channel) {
  //The tenth channel is **always** a drumset type instrument. Never play it
  if(channel == 9) {
    return 0;
  }
  return playChannels[channel];
}

void resetPlayChannels() {
  int i = 0;
  for(i=0 ; i < 16; i++) {
    playChannels[i] = 1;
  }
}


void midi_process(snd_seq_event_t *ev)
{
    //If this event is a PGMCHANGE type, it's a request to map a channel to an instrument
    if( ev->type == SND_SEQ_EVENT_PGMCHANGE )  {
       printf("PGMCHANGE: channel %2d, %5d, %5d\n", ev->data.control.channel, ev->data.control.param,  ev->data.control.value);

       //Clear pins state, this is probably the beginning of a new song
       clearPinsState();
       

       //Filter out this channel if it's a base, percussion, or synth instrument
       if(
           (ev->data.control.value >= 8 && ev->data.control.value <= 15) ||  //Percussion
           (ev->data.control.value >= 32 && ev->data.control.value <= 39) || //Base
           (ev->data.control.value >= 88 && ev->data.control.value <= 103)   //Synth
        
       ) {
          setPlayChannel(ev->data.control.channel, 0);
       }
       else {
          setPlayChannel(ev->data.control.channel, 1);
       }
    }

    //Note on/off event
    else if ( ((ev->type == SND_SEQ_EVENT_NOTEON)||(ev->type == SND_SEQ_EVENT_NOTEOFF)) ) {
        
       //If it's on a channel I care about
       if( isPlayChannel(ev->data.note.channel) ) {
       
          int isOn = 1;
          //Note velocity == 0 means the same thing as a NOTEOFF type event
          if( ev->data.note.velocity == 0 || ev->type == SND_SEQ_EVENT_NOTEOFF) {
             isOn = 0;
          }
  

          //There are 12 different kinds of notes.
          int noteMod = ev->data.note.note % 12;

          //Cast to double
          double noteModDouble = noteMod;

          //The pin to use is determined by:
          // ( pitch  /  ( Total number of notes / Total Number of Pins) )
          double noteBin = noteModDouble / (12.0 / MY_NUM_PINS); 
         
          //Cast back to int
          int pinIdx = (int)noteBin;

          //If pin is set to be turned on
          if( isOn ) {
             //If pin is currently available to play a note, or if currently playing channel can be overriden due to higher priority channel
             if( pinNotes[pinIdx] == -1 || pinChannels[pinIdx] > ev->data.note.channel )  {
                    
                if( (pinChannels[pinIdx] > ev->data.note.channel ) && pinNotes[pinIdx] != -1)  {
                   printf("OVERRIDING CHANNEL %i for %i\n", pinChannels[pinIdx], ev->data.note.channel);
                }
                //Write to the pin, save the note to pinNotes
                //printf("Pin %i - %s %i %i \n", pinIdx, isOn ? "on" : "off", ev->data.note.note, ev->data.note.channel);       
                digitalWrite(pinMap[pinIdx], 1); 
                digitalWrite(pinMap2[pinIdx], 1); 
                pinNotes[pinIdx] = ev->data.note.note;
                pinChannels[pinIdx] =  ev->data.note.channel;
             }
          }
        
          //Pin is to be turned off
          else {
             //If this is the note that turned the pin on..
             if( pinNotes[pinIdx] == ev->data.note.note && pinChannels[pinIdx] == ev->data.note.channel ) {
                //Write to the pin, indicate that pin is available
                //printf("Pin %i - %s %i %i \n", pinIdx, isOn ? "on" : "off", ev->data.note.note, ev->data.note.channel);       
                digitalWrite(pinMap[pinIdx], 0); 
                digitalWrite(pinMap2[pinIdx], 0);
                pinNotes[pinIdx] = -1;
                pinChannels[pinIdx] = INT_MAX;
             }
          }
       }
    }
    
    else {
      //printf("Unhandled event %2d\n", ev->type);
      ;
    }

    snd_seq_free_event(ev);
}

void print_data(snd_seq_event_t *ev){
  printf("(%i,  %i, %2d, %5d, %5d)\n", ev->data.note.note, ev->data.note.channel, ev->data.control.channel, ev->data.control.param,  ev->data.control.value); 
  
}

int main()
{

    //Start as a daemon
    //if( daemon(0,0) != 0) {
    //  exit(1);
    //}
    
    //Setup wiringPi
    if( wiringPiSetupGpio() == -1) {
      exit(1);
    }
   
    //Setup all the pins to use OUTPUT mode
    int i=0;
    for(i=0; i< MY_NUM_PINS; i++) {
      pinMode(pinMap[i], OUTPUT);
      pinMode(pinMap2[i], OUTPUT);
    }


    clearPinsState();
    resetPlayChannels();

    //Open a midi port, connect to thru port also
    midi_open();

    //Process events forever
    while (1) {
       midi_process(midi_read());
       //print_data(midi_read());
    }

    return -1;
}