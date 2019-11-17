#include <Wire.h>
#include <SD.h>                      // need to include the SD library
//#define SD_ChipSelectPin 53  //example uses hardware SS pin 53 on Mega2560
#define SD_ChipSelectPin 4  //using digital pin 4 on arduino nano 328, can use other pins
#include <TMRpcm.h>           //  also need to include this library...
#include <SPI.h>

TMRpcm tmrpcm;

uint8_t music = 0;
uint8_t sound = 0;

unsigned long time = 0;

void setup(){
  tmrpcm.speakerPin = 9; 
  
  Wire.begin(0x12); 
  Wire.onReceive(receiveEvent);
}

void loop() {
  
  if(tmrpcm.isPlaying() && millis() - time > 50 ) {      
        time = millis();    
  }else
  if(millis() - time > 500){     
      time = millis(); 
  }

  switch(music){
    case 1: tmrpcm.play("1.wav"); break;
    case 2: tmrpcm.play("2.wav"); break;
    default: break;
  }

  if(sound == 1){
    tmrpcm.volume(1);
  }else{
    tmrpcm.volume(0);
  }
}

void receiveEvent(int bytes) {
  if(bytes>1){
    music = Wire.read();
    sound = Wire.read();
  }
}
