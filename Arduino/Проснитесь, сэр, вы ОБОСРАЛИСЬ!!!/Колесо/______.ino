#include <Wire.h>

uint8_t _speed = 0;
uint8_t light = 0;

void setup() {
  pinMode(3, OUTPUT);
  pinMode(5, OUTPUT);

  Wire.begin(0x11); 
  Wire.onReceive(receiveEvent);
}

void loop() {
  analogWrite(3, _speed);
  analogWrite(5, light);
}

void receiveEvent(int bytes) {
  if(bytes>1){
    _speed = Wire.read();
    light = Wire.read();
  }
}
