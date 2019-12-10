#include <Wire.h>
#include <TroykaThermometer.h>

// red pin 5, green pin 6, blue pin 9
#define HOT_PIN 3

double bright = 1;
long long int tim = 0;
uint8_t temp = 0, temperature = 30, light[3] = {255, 255, 255}, light_pin[3] = {5, 6, 9};
uint8_t sensor = 0;

TroykaThermometer thermometer(A0);

void setup() {
  Serial.begin(9600);
  
  pinMode(HOT_PIN,OUTPUT); 
  for(int i = 0; i < 3; i++)
    pinMode(light_pin[i], OUTPUT);
    
//  Wire.begin(0x12); 
//  Wire.onReceive(receiveEvent);
//  Wire.onRequest(requestEvent);
}

void loop() {
  thermometer.read();
  sensor = thermometer.getTemperatureC();
  temp = min(max(0, (temperature - sensor)*100), 255);

  Serial.println(sensor);

  analogWrite(HOT_PIN, temp);
  for(int test = 0; test < 6; test++){  
    if(test > 3)
      light[test%3] = 255;
    else
      light[test] = 0;
      
    for(int i = 0; i < 3; i++)
      analogWrite(light_pin[i], light[i]);
    
    Serial.println(test);

    delay(1000);
  }
  if(millis() - tim > 1000){
     tim = millis();
     Serial.println("hello");
  }
}

void receiveEvent(int bytes) {
  if(bytes > 1){
    temperature = Wire.read();
    bright = double(Wire.read()) / 100;
    for(int i = 0; i < 3; i++)
      light[i] = double(Wire.read() * bright) / 100 * 255;

    Serial.println("start reading");
    Serial.println(temperature);
    Serial.println(bright);
    for(int i = 0; i < 3; i++)
      Serial.println(light[i]);
    Serial.println("end reading");
  }
}

void requestEvent(){
  Wire.write((uint8_t *)&sensor, sizeof(&sensor));
}
