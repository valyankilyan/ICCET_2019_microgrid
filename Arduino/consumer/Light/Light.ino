#include <Wire.h>

#define RED_PIN 2
#define GREEN_PIN 3
#define BLUE_PIN 5


uint8_t bright = 255;
uint8_t light[3] = {255, 255, 255};

void setup() {
  
  pinMode(RED_PIN,OUTPUT); 
  pinMode(GREEN_PIN,OUTPUT); 
  pinMode(BLUE_PIN,OUTPUT); 

  Wire.begin(0x13); 
  Wire.onReceive(receiveEvent);
}

void loop() {
  analogWrite(RED_PIN, light[0]);
  analogWrite(GREEN_PIN, light[1]);
  analogWrite(BLUE_PIN, light[2]);
}

void receiveEvent(int bytes) {
  if(bytes>1){
    bright = Wire.read();
    for(int i = 0; i < 3; i++)
      light[i] = map(Wire.read(), 0, 100, 0, 256) * bright / 100;
  }
}
