#include <SD.h>              
#define SD_ChipSelectPin 10  
#include <TMRpcm.h>          
#include <SPI.h>
#include <Wire.h>

#define SOUND_SIZE 6
 
TMRpcm tmrpcm;
 
bool work = 1, replay = 0;
int sound_id = 1, old_sound_id = 0, boost = 0, old_boost = 0;
long long int last_music_time = 0, tim = 0 ; 

char* music_list[SOUND_SIZE] = {
  "SILENSE",
  "Shrek.wav",
  "otvinta.wav",
  "Soccer.wav",
  "dimooon.wav",
  "John.wav"
  };
  
long long int music_len[SOUND_SIZE] = {
  99999999,//silence
  132500,//"Shrek theme", 
  204000,//"From Vint", 
  310000,//"Soccer.wav", 
  66000,//"Dmitry"
  21000//"John.wav"
  };
 
void setup(){
  Wire.begin(0x10);
  Wire.onReceive(receiveEvent);
  
  Serial.begin(9600);
  
  tmrpcm.speakerPin = 9;
  SD.begin(SD_ChipSelectPin);
  
  Serial.println("Start");
}
 
 
void loop(){  
  if(tim - millis() > 10000){
    Serial.println("it works");
    tim = millis();
  }
  while(boost != old_boost){
    tmrpcm.volume(boost > old_boost); 
    old_boost+= (boost > old_boost ? 1 : -1);  
  } 

  if(millis() - last_music_time > music_len[sound_id]){
    if(replay)
      old_sound_id--;
    else
      sound_id = (sound_id)%(SOUND_SIZE - 1) + 1;
    //sound_id = (sound_id % (SOUND_SIZE - 1)) + 1;
  }
  
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
    sound_id = Wire.read() % SOUND_SIZE;
    boost = Wire.read() % 5;
    replay = Wire.read();
    Serial.print("sound_id = ");
    Serial.println((int)sound_id);
    Serial.print("boost = ");
    Serial.println(boost);
  }
}
