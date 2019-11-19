#include <Wire.h>
#include <TroykaThermometer.h>

uint8_t temp = 0;
uint8_t light_1 = 0;
uint8_t light_2 = 0;
uint8_t light_3 = 0;

uint8_t sensor = 0;

TroykaThermometer thermometer(A0);

void setup() {
  
  
  pinMode(3,OUTPUT); 
  pinMode(5,OUTPUT); 
  pinMode(6,OUTPUT);
  pinMode(9,OUTPUT);  

  Wire.begin(0x14); 
  Wire.onReceive(receiveEvent);
  Wire.onRequest(requestEvent);
}

void loop() {
  
  thermometer.read();
  sensor = thermometer.getTemperatureC();
  
  analogWrite(3, temp);
  analogWrite(4, 255*(light_1/100));
  analogWrite(6, 255*(light_2/100));
  analogWrite(9, 255*(light_3/100));

  if(sensor > 45)
    temp = 0;
  if(sensor < 30)
    temp = 255;
}

void receiveEvent(int bytes) {
  if(bytes>1){
    temp = Wire.read();
    light_1 = Wire.read();
    light_2 = Wire.read();
    light_3 = Wire.read();
  }
}

void requestEvent(){
  Wire.write((uint8_t *)&sensor, sizeof(&sensor));
}

