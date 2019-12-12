#include <SD.h>                      // need to include the SD library
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
    analogWrite(light_pin[i], light[i]);

  if(millis() - tim > 1000){
     tim = millis();
     Serial.println("hello");
  }
  delay(50);
}

void receiveEvent(int byteCount){

  while(Wire.available()) {
    temperature = Wire.read();
    bright = double(Wire.read()) / 100;
    for(int i = 0; i < 3; i++)
      light[i] = double(Wire.read() * bright) / 100 * 255;
    Wire.read();

    Serial.println("start reading");
    Serial.println(temperature);
    Serial.println(bright);
    for(int i = 0; i < 3; i++)
      Serial.println(light[i]);
    Serial.println("end reading");
  }
}

void requestEvent(){
  Wire.write(temperature);
  Wire.write(uint8_t(bright * 100));
  for(int i = 0; i < 3; i++)
    Wire.write(light[i]);
  Wire.write(sensor);
}
/*
#include <Wire.h>

#define SLAVE_ADDRESS 0x12
int number = 0;
int state = 0;

void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600); // start serial for output
  
  Wire.begin(SLAVE_ADDRESS);

 
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);

  Serial.println("Ready!");
}

void loop() {
  delay(100);
}

void receiveData(int byteCount){

  while(Wire.available()) {
    number = Wire.read();
    Serial.print("data received: ");
    Serial.println(number);

    if (number == 1){
      if (state == 0){
        digitalWrite(13, HIGH); // set the LED on
        state = 1;
      }
      else{
        digitalWrite(13, LOW); // set the LED off
        state = 0;
      }
    }
  }
}

  
void sendData(){
  Wire.write(number);
}*/
