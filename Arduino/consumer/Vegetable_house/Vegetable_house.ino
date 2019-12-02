#include <Wire.h>
#include <TroykaThermometer.h>

uint8_t temp = 0, temperature = 30, brightness = 0, light[3] = {0, 0, 0}, light_pin[3] = {5, 6, 9};

uint8_t sensor = 0;

TroykaThermometer thermometer(A0);

void setup() {
  
  
  pinMode(3,OUTPUT); 
  for(int i = 0; i < 3; i++)
    pinMode(light_pin[i], OUTPUT);

  Wire.begin(0x14); 
  Wire.onReceive(receiveEvent);
  Wire.onRequest(requestEvent);
}

void loop() {
  
  thermometer.read();
  sensor = thermometer.getTemperatureC();
  temp = min((temperature - sensor)*100, 255);
  
  analogWrite(3, temp);
  for(int i = 0; i < 3; i++)
    analogWrite(light_pin[i], light[i] * 255 / 100 * brightness);

}

void receiveEvent(int bytes) {
  if(bytes>1){
    temperature = Wire.read();
    brightness = Wire.read();
    for(int i = 0; i < 3; i++)
      light[i] = Wire.read();
  }
}

void requestEvent(){
  Wire.write((uint8_t *)&sensor, sizeof(&sensor));
}
