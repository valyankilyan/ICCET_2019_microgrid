#include <Wire.h>

#define RED_PIN 2
#define GREEN_PIN 3
#define BLUE_PIN 5
#define MOUNTAIN_PIN 10

double bright = 1; 
uint8_t mountain_bright = 255;
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
  for(int i = 0; i < 6; i++){
    if(i > 3)
      light[i%3] = 255;
    else
      light[i] = 0;

    analogWrite(RED_PIN, light[0]);
    analogWrite(GREEN_PIN, light[1]);
    analogWrite(BLUE_PIN, light[2]);
    analogWrite(MOUNTAIN_PIN, mountain_bright);

    delay(1000);
  }
  
  analogWrite(RED_PIN, light[0]);
  analogWrite(GREEN_PIN, light[1]);
  analogWrite(BLUE_PIN, light[2]);
  analogWrite(MOUNTAIN_PIN, mountain_bright);

  
}

void receiveEvent(int bytes) {
  if(bytes>1){
    bright = (double)Wire.read()/100;
    for(int i = 0; i < 3; i++)
      light[i] = map(Wire.read(), 0, 100, 0, 255) * bright;
    mountain_bright = map(Wire.read(), 0, 100, 0, 255) * bright;
  }
}
