#include <SD.h>                      // need to include the SD library
//#define SD_ChipSelectPin 53  //example uses hardware SS pin 53 on Mega2560
#define SD_ChipSelectPin 10  //using digital pin 4 on arduino nano 328, can use other pins
#include <TMRpcm.h>           //  also need to include this library...
#include <SPI.h>
#include <Wire.h>
 
TMRpcm tmrpcm;   // create an object for use in this sketch
 
bool work = 1;
int sound_id = 2, old_sound_id = 0;
bool boost = 0, old_boost = 0;
long long int last_music_time = 0; 

char* music_list[9] = {
  "SILENSE",
  "Soccer.wav",
  "Shrek.wav",
  "nevergonna.wav",
  "nevernever.wav",
  "otvinta.wav",
  "golosovanie.wav",
  "dimooon.wav",
  "John.wav"
  };
  
long long int music_len[9] = {
  99999999,//silence
  310000,//"Soccer.wav", 
  133000,//"Shrek theme", 
  212000,//"Never gonna give you up", 
  251000,//"Never, never give you ya up", 
  204000,//"From Vint", 
  240000,//"Votting", 
  66000,//"Dmitry"
  21000//"John.wav"
  };
 
void setup(){
  Wire.begin(0x10);
  Wire.onReceive(receiveEvent);
  Serial.begin(9600);
  tmrpcm.speakerPin = 9; //5,6,11 or 46 on Mega, 9 on Uno, Nano, etc
  SD.begin(SD_ChipSelectPin);
  Serial.println("Start");
}
 
 
void loop(){  
  if(old_boost != boost){
    old_boost = boost;
    tmrpcm.volume(boost);
    }

  //if(millis() - last_music_time > music_len[sound_id]){
  //  sound_id = ((sound_id+1) % 8) + 1;
  //}
  
  if(old_sound_id != sound_id){    
    old_sound_id = sound_id;
    last_music_time = millis();
    
      if(sound_id == 0)
        tmrpcm.stopPlayback(); 
      else
        tmrpcm.play(music_list[sound_id]);

      Serial.println(music_list[sound_id]);
  }
}
 
void receiveEvent(int bytes) {
  if(bytes > 1){
    sound_id = Wire.read();
    boost = Wire.read();
    Serial.println((int)sound_id);
    work = Wire.read();
    Serial.println(work);
  }
}
