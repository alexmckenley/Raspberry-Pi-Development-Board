/* Raspberry Pi to Arduino 
Serial port expander
*/
const byte pins[] = {8,7,6,5};
const byte pinsAnalog[] = {17,16,15,14};

byte first = 0;
byte value = 0;
byte analogAsDigital = 0;

byte x;


void setup(){
  Serial.begin(115200);
  
  analogReference(EXTERNAL);
  
  for(x = 0; x<4; x++)
    pinMode(pins[x], INPUT);
  
}


void loop(){
  if (Serial.available() > 0){
    first = Serial.read();
    //Serial.write(first);
    if ((bitRead(first, 7) == 0) && (bitRead(first,6) == 1)){
      while(Serial.available() < 1);
      value = Serial.read();
      //Serial.write(value);
    }
    

    
    if (first & (1<<7))
      setMode();
    else{
      //If bit 6 == 1 then SET if 0, then GET
      if(first & (1<<6))
        set();
      else
        get();
    }
  }
  
}

void setMode(){
  //If bit 5 is 1 then set DIGITAL pin, if 0, set ANALOG pin);
  //This function completely ignores the second byte 'value'
  //Return 0xFF when complete
  


  if(first & (1<<5)){
    for( x = 0; x < 4; x++){
        pinMode(pins[x], bitRead(first,x));
    }
  }
  else{
    for( x = 0; x < 4; x++){
      pinMode(pinsAnalog[x], bitRead(first,x));
      if (bitRead(first,x) == 0)
        bitClear(analogAsDigital, x);
      else
        bitSet(analogAsDigital, x);
    }
  }

  Serial.write(255);
}

void set(){
  //Set the specified pin, and return 0xFF.
  
    //Check first for PWM flag
  if(first & (1<<4)){
    for (x = 2; x < 4; x++){
      if(bitRead(first,x))
        analogWrite(pins[x], value);
    }

  }
  else{
    if(first & (1<<5)){
      //Run through the last four bits of first
      for( x = 0; x < 4; x++){
        //If one of the bits is 1, write value to that pin.
        if(bitRead(first,x))
          digitalWrite(pins[x], value);
      }
    }
    else{
      for( x = 0; x < 4; x++){
        if(bitRead(first,x) && bitRead(analogAsDigital, x))
          digitalWrite(pinsAnalog[x], value);
      }
    }
  }
  Serial.write(255);
}

void get(){
  //Get the specified pin, and return the value.
  if(first & (1<<5)){
    for( x = 0; x < 4; x++){
      if(bitRead(first,x)){
        Serial.write(digitalRead(pins[x]));
        return;
      }
    }
  }
  else{
    for( x = 0; x < 4; x++){
      if(bitRead(first,x) && (bitRead(analogAsDigital, x)==0)){
        //Serial.write(pinsAnalog[x]);
        Serial.write(analogRead(pinsAnalog[x])/4);
      }
    }
  }
  
}

