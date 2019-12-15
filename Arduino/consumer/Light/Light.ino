#include <Wire.h>

#define MOUNTAIN_PIN 10

uint8_t mountain_bright = 1;
int light_pins[3] = {2, 3, 5};
uint8_t light[3] = {255, 255, 255};

void setup() {  
  for(int i = 0; i < 3; i++)
    pinMode(light_pins[i], OUTPUT);  
  pinMode(MOUNTAIN_PIN, OUTPUT);

  Wire.begin(0x11); 
  Wire.onReceive(receiveEvent);
}

void loop() {
  for(int i = 0; i < 3; i++)
    analogWrite(light_pins[i], light[i]);
  digitalWrite(MOUNTAIN_PIN, mountain_bright);
}

void receiveEvent(int bytes) {
  if(bytes>1){
    for(int i = 0; i < 3; i++)
      light[i] = map(Wire.read(), 0, 100, 0, 255);
    mountain_bright = Wire.read();
  }
}
