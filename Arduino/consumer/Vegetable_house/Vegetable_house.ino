#include <Wire.h>
#include <TroykaThermometer.h>

// red pin 5, green pin 6, blue pin 9
#define HOT_PIN 3

double bright = 0;
uint8_t temp = 0, temperature = 30, light[3] = {0, 0, 0}, light_pin[3] = {5, 6, 9};
uint8_t sensor = 0;

TroykaThermometer thermometer(A0);

void setup() {
  pinMode(HOT_PIN,OUTPUT); 
  for(int i = 0; i < 3; i++)
    pinMode(light_pin[i], OUTPUT);

  Wire.begin(0x12); 
  Wire.onReceive(receiveEvent);
  Wire.onRequest(requestEvent);
}

void loop() {
  thermometer.read();
  sensor = thermometer.getTemperatureC();
  temp = min(max(0, (temperature - sensor)*100), 255);
  
  analogWrite(HOT_PIN, temp);
  for(int i = 0; i < 3; i++)
    analogWrite(light_pin[i], light[i]);

}

void receiveEvent(int bytes) {
  if(bytes>1){
    temperature = Wire.read();
    bright = double(Wire.read()) / 100;
    for(int i = 0; i < 3; i++)
      light[i] = map(Wire.read(), 0, 100, 0, 256) * bright / 100;
  }
}

void requestEvent(){
  //Wire.write((uint8_t *)&sensor, sizeof(&sensor));
}
