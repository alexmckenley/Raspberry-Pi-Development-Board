/* Serial Communication program to extend
Raspberry Pi GPIO.
For use with Alex Taylors Raspberry Pi 
Development board.


Serial data should be send in the following format with no
spaces or punctuation.

-Getting:
  (Instruction)(Port)(Channel)
  (S,G)(A,D)(0-3)
-Setting:
  (Instruction)(Port)(Channel)(Value)
  (S,G)(A,D)(0-3)([0-255],[0,1])
-Initializing a pin:
  (Instruction)(Channel)(Direction)
  (X)(0-3)(I,O)

*/
const int pins[] = {5,6,7,8};

char instruction;
char port;
char temp;
int channel;
int value;
int dir;

void setup(){
 Serial.begin(115200);
 
 //setup digital Pins as input by default 
 pinMode(pins[0], INPUT);
 pinMode(pins[1], INPUT);
 pinMode(pins[2], INPUT);
 pinMode(pins[3], INPUT);
}

void loop(){
  if(Serial.available() > 0){
    instruction = Serial.read();
    switch (instruction){
      case 'G':
        Serial.write('G');
        get();
        break;
      case 'S':
      Serial.write('S');
        set();
        break;
      case 'X':
        Serial.write('X');
        setupPin();
        break;
      default:
        Serial.write('Z');
        break;
    }
  }
}


void get(){
  while(Serial.available() <= 0);
  port = Serial.read();
  Serial.write(port);
  while(Serial.available() <= 0);
  temp = Serial.read();
  //channel = atoi(&temp);
  channel = (int)temp;
  channel = channel - 48;
  //channel = constrain(channel,0,3);
  
  if (port == 'A'){
    Serial.write(analogRead(channel)/4);
    delay(10);
  }
  else if (port == 'D'){
    Serial.write(digitalRead(pins[channel]));
    delay(10);
  }
  

  
}

void set(){
  while(Serial.available() < 3);
  port = Serial.read();
  channel = Serial.parseInt();
  channel = constrain(channel,0,3);
  value = Serial.parseInt();
  if (port == 'A'){
    channel = constrain(channel,0,1);
    value = constrain(value,0,255);
    analogWrite(pins[channel], value);
  }
  if (port == 'D'){
    value = constrain(value, 0,1);
    digitalWrite(pins[channel], value);
  }
}

void setupPin(){
  while(Serial.available() < 2);
  channel = Serial.parseInt();
  channel = constrain(channel,0,3);
  dir = Serial.read();
  if (dir == 'I')
    pinMode(pins[channel], INPUT);
  else if (dir == 'O')
    pinMode(pins[channel], OUTPUT);
  
}

