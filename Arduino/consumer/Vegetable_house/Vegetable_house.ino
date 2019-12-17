#include <Wire.h>
#include <TroykaThermometer.h>

#define HOT_PIN 3 

double bright = 1;
int light_pins[3] = {10, 5, 6};
uint8_t light[3] = {255, 255, 255}, temperature;

uint8_t sensor = 0;

TroykaThermometer thermometer(A0);

void setup() {  
  Serial.begin(9600);
  
  for(int i = 0; i < 3; i++)
    pinMode(light_pins[i], OUTPUT);  
  pinMode(HOT_PIN, OUTPUT);

  Wire.begin(0x12); 
  Wire.onReceive(receiveEvent);
  Wire.onRequest(requestEvent);
}

void loop() {
  thermometer.read();
  sensor = thermometer.getTemperatureC();
  int temp = min(max(0, (temperature - sensor)*100), 255);
  analogWrite(HOT_PIN, temp);
  
  for(int i = 0; i < 3; i++)
    analogWrite(light_pins[i], light[i] * bright);
  digitalWrite(HOT_PIN, temp);
}

void receiveEvent(int bytes) {
  if(bytes>1){
    temperature = Wire.read();
    bright = (double)Wire.read() / 100;
    for(int i = 0; i < 3; i++)
      light[i] =  double(Wire.read()) / 100 * 255;

    Serial.print(temperature);
    Serial.print(" ");
    Serial.print(bright);
    Serial.print(" ");
    for(int i = 0; i < 3; i++){
      Serial.print(light[i]);
      Serial.print(" ");
    }
    Serial.println(" ");
  }
}

void requestEvent(){
  Serial.println("write");
  Wire.write(temperature);
  Wire.write(uint8_t(bright * 100));
  for(int i = 0; i < 3; i++)
    Wire.write(light[i]);
  Wire.write(sensor);
}
/*

#include <SD.h>                      // need to include the SD library
#include <Wire.h>
#include <TroykaThermometer.h>

// red pin 5, green pin 6, blue pin 9
#define HOT_PIN 3 

double bright = 1;
long long int tim = 0;
uint8_t temp = 0, temperature = 30;
 
int light_pins[3] = {6, 10, 5};
uint8_t light[3] = {255, 255, 255};

uint8_t sensor = 0;

TroykaThermometer thermometer(A0);

void setup() {
  Serial.begin(9600);
  
  pinMode(HOT_PIN,OUTPUT); 
  for(int i = 0; i < 3; i++)
    pinMode(light_pins[i], OUTPUT);

  Wire.begin(0x12); 
  Wire.onReceive(receiveEvent);
  Wire.onRequest(requestEvent);
}

void loop() {
  thermometer.read();
  sensor = thermometer.getTemperatureC();
  temp = min(max(0, (temperature - sensor)*100), 255);
  
  analogWrite(HOT_PIN, 255);
  
  for(int i = 0; i < 3; i++)
    analogWrite(light_pins[i], (double)light[i] * bright / 100 * 255);

  if(millis() - tim > 10000){
     tim = millis();
     Serial.println("hello");
  }
}

void receiveEvent(int bytes){

  if(bytes > 1) {
    temperature = Wire.read();
    bright = max(0, (double)Wire.read()/100);
    for(int i = 0; i < 3; i++)
      light[i] =  Wire.read();

//    Serial.println("start reading");
    Serial.print(temperature);
    Serial.print(" ");
    Serial.print(bright);
    Serial.print(" ");
    for(int i = 0; i < 3; i++){
      Serial.print(light[i]);
      Serial.print(" ");
    }
    Serial.println(" ");
//    Serial.println("end reading");
  }
}

void requestEvent(){
  Serial.println("write");
  Wire.write(temperature);
  Wire.write(uint8_t(bright * 100));
  for(int i = 0; i < 3; i++)
    Wire.write(light[i]);
  Wire.write(sensor);
}*/
