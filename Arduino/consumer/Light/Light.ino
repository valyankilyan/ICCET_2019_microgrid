#include <Wire.h>

#define RED_PIN 2
#define GREEN_PIN 3
#define BLUE_PIN 5
#define MOUNTAIN_PIN 10

uint8_t bright = 255, mountain_bright = 255;
uint8_t light[3] = {255, 255, 255};

void setup() {
  
  pinMode(RED_PIN,OUTPUT); 
  pinMode(GREEN_PIN,OUTPUT); 
  pinMode(BLUE_PIN,OUTPUT); 
  pinMode(MOUNTAIN_PIN, OUTPUT);

  Wire.begin(0x11); 
  Wire.onReceive(receiveEvent);
}

void loop() {
  analogWrite(RED_PIN, light[0]);
  analogWrite(GREEN_PIN, light[1]);
  analogWrite(BLUE_PIN, light[2]);
  analogWrite(MOUNTAIN_PIN, mountain_bright);
}

void receiveEvent(int bytes) {
  if(bytes>1){
    bright = Wire.read();
    for(int i = 0; i < 3; i++)
      light[i] = map(Wire.read(), 0, 100, 0, 256) * bright / 100;
    mountain_bright = Wire.read();
  }
}
