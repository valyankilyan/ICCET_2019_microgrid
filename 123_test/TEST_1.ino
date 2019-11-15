#include <SD.h>
//#include "TMRpcm.h"
#include "SPI.h"
#include <Wire.h>
#include "ACS712.h"
#include "SPI.h"
 
#define SD_ChipSelectPin 10
 
#define ADDRES 16
#define SPEAKER_PIN 5
#define R_PIN 3 //6
#define G_PIN 9 //3dadada  9
#define B_PIN 6 //3
 
 
uint8_t song = 0;
uint8_t last_song = 0;
uint8_t g = 255;
uint8_t r = 1;
uint8_t b = 255;

int who;
 
struct Block{
  uint8_t from;
  float how;
  float when;
}block;
 
int last_t = 0;//таймер
 
//float when_repiat = 0; // в данную переменную запихиваем время, с которого происходит передача, а так как блоки формируются каждые 500 мс, то...
int P = 0;//потребление тока в ваттсекунда
 
ACS712 sensor_1(ACS712_20A, A1);
 
void setup() {
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
 
  pinMode(SPEAKER_PIN,  OUTPUT);
  pinMode(R_PIN,  OUTPUT);
  pinMode(G_PIN,  OUTPUT);
  pinMode(B_PIN ,  OUTPUT);
 
  Wire.begin(ADDRES);                // join i2c bus with address #8
  Wire.onReceive(receiveEvent); // register event
  Wire.onRequest(requestEvent);
  Serial.begin(9600);           // start serial for output
 
  last_t = millis();
}
 
void loop() {
  if(last_t - millis() > 100){
    if(last_song != song)
      _play();
 
    float I_1 = sensor_1.getCurrentAC();
 
    P += I_1 /*time*/ * 9 * last_t;
    last_t = millis();
    if(last_t % 3 == 500){
      Serial.print('P = ');
      Serial.println(P);  
    }
  }
  //delay(100);
}
 
void receiveEvent(int how_many) {
  //while (1 < Wire.available()) { // loop through all but the last
    int a = Wire.read();
    Serial.print("a = ");
    Serial.println(a);
    if(a != -1){
      //Serial.println(a);
      if(who % 3 == 0)
        r = a;
        analogWrite(R_PIN, r);//light_green
      if(who % 3 == 1)
        g = a;
        analogWrite(G_PIN, g);//light_red
      if(who % 3 == 2)
        b = a;
        analogWrite(B_PIN, b);//light_red
      who++;
    }
 // }
  //int x = Wire.read();    // receive byte as an integer
  //Serial.println(x);         // print the integer
}
void requestEvent() {
  Wire.write((uint8_t *)&P, sizeof(P));
}
 
void _play(){
 
  last_song = song;
  }
 
/*#include <SD.h>
#include "TMRpcm.h"
#include "SPI.h"
#include <Wire.h>
#include "ACS712.h"
#include "SD.h"
 
#define SD_ChipSelectPin 10
 
//TMRpcm tmrpcm;
 
#define ADDRES 16
#define SPEAKER_PIN 3
#define R_PIN 5
#define G_PIN 6
#define B_PIN 9
 
 
uint8_t song = 0;
uint8_t last_song = 0;
uint8_t g = 1;
uint8_t r = 1;
uint8_t b = 1;
 
struct Block{
  uint8_t from;
  float how;
  float when;
}block;
 
int last_t = 0;//таймер
 
float when_repiat = 0; // в данную переменную запихиваем время, с которого происходит передача, а так как блоки формируются каждые 500 мс, то...
int P = 0;//потребление тока в ваттсекунда
 
ACS712 sensor_1(ACS712_20A, A1);
 
void setup() {
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
 
  //tmrpcm.setVolume(6);
  //tmrpcm.speakerPin = SPEAKER_PIN;
 
  pinMode(R_PIN,  OUTPUT);
  pinMode(G_PIN,  OUTPUT);
  pinMode(B_PIN ,  OUTPUT);
 
  Wire.begin(ADDRES);                // join i2c bus with address #8
  Wire.onReceive(receiveEvent); // register event
  Wire.onRequest(requestEvent);
  Serial.begin(9600);           // start serial for output
 
  last_t = millis();
}
 
void loop() {
  if(last_t - millis() > 100){
    unsigned long time = millis();        
    //if(last_song != song)
    //  _play();
    analogWrite(R_PIN, r);//light_green
    analogWrite(G_PIN, g);//light_red
    analogWrite(B_PIN, b);//light_red
 
    float I_1 = sensor_1.getCurrentAC();
    float U = analogRead(A6);
 
    P += I_1 * time * U;
    last_t = millis();
  }
  //delay(100);
}
 
void receiveEvent() {
  while (1 < Wire.available()) { // loop through all but the last
    int a = Wire.read();
    int b = Wire.read();
    int c = Wire.read();
 
    if(a == 0x01 && b == 0x02 && c == 0x03){
          song = Wire.read();
          r = Wire.read();
          g = Wire.read();
          b = Wire.read();
          Serial.print(song);
          Serial.print(" | ");
          Serial.print(r);
          Serial.print(" | ");
          Serial.print(g);
          Serial.print(" | ");
          Serial.println(b);
    }
  }
  //int x = Wire.read();    // receive byte as an integer
  //Serial.println(x);         // print the integer
}
void requestEvent() {
  Wire.write((uint8_t *)&P, sizeof(P));
}
 
/*void _play(){
 
  last_song = song;
  switch(song){
    case 0:
      digitalWrite(SPEAKER_PIN, 0);
    case 1:
      tmrpcm.play("1.wav");
      break;
    case 2:
      tmrpcm.play("2.wav");
      break;
  }
}*/
