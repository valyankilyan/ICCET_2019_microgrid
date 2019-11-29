#include <SD.h>                      // need to include the SD library
//#define SD_ChipSelectPin 53  //example uses hardware SS pin 53 on Mega2560
#define SD_ChipSelectPin 10  //using digital pin 4 on arduino nano 328, can use other pins
#include <TMRpcm.h>           //  also need to include this library...
#include <SPI.h>
#include <Wire.h>
 
TMRpcm tmrpcm;   // create an object for use in this sketch
 
bool work = 1;
int sound_id = 3;
int old_sound_id = 3;
 
void setup(){
  Wire.begin(0x10);
  Wire.onReceive(receiveEvent);
  Serial.begin(9000);
  tmrpcm.speakerPin = 9; //5,6,11 or 46 on Mega, 9 on Uno, Nano, etc
  SD.begin(SD_ChipSelectPin);
  tmrpcm.play("3.wav"); //the sound file "music" will play each time the arduino powers up, or is reset
}
 
 
 
void loop(){  
  if(old_sound_id != sound_id){
    if(sound_id == 1){ //send the letter p over the serial monitor to start playback
      tmrpcm.play("1.wav");
      old_sound_id = sound_id;
    }    
    if(sound_id == 2){ //send the letter p over the serial monitor to start playback
      tmrpcm.play("2.wav");
      old_sound_id = sound_id;
    }
    if(sound_id == 3){ //send the letter p over the serial monitor to start playback
      tmrpcm.play("3.wav");
      old_sound_id = sound_id;
    }
  }
}
 
void receiveEvent(int bytes) {
  if(bytes > 1){
    sound_id = Wire.read();
    Serial.println((int)sound_id);
    work = Wire.read();
    Serial.println(work);
  }
}
