#include <Wire.h>

uint8_t on = 0;

void setup() {
  pinMode(2, OUTPUT);

  Wire.begin(0x10); 
  Wire.onReceive(receiveEvent);
}

void loop() {
  analogWrite(2, 255*on);
}

void receiveEvent(int bytes) {
  if(bytes>1)
    on = Wire.read();
}



