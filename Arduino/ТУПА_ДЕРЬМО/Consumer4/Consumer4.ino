#include <Wire.h>

uint8_t lamp = 0;
uint8_t light_1 = 0;
uint8_t light_2 = 0;
uint8_t light_3 = 0;

void setup() {
  
  pinMode(2,OUTPUT); 
  pinMode(3,OUTPUT); 
  pinMode(5,OUTPUT); 
  pinMode(6,OUTPUT); 

  Wire.begin(0x12); 
  Wire.onReceive(receiveEvent);
}

void loop() {
  
  analogWrite(2, 255*lamp);
  analogWrite(2, light_1);
  analogWrite(2, light_2);
  analogWrite(2, light_3);
  
}

void receiveEvent(int bytes) {
  if(bytes>1){
    lamp = Wire.read();
    light_1 = Wire.read();
    light_2 = Wire.read();
    light_3 = Wire.read();
  }
}
