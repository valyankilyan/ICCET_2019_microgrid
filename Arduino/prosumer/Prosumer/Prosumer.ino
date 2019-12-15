// Этот код обязательно для Arduino Nano или Arduino Mega

#include "ACS712.h"
#include <Wire.h>

float R1 = 100000.0; // resistance of R1 (100K) 
float R2 = 10000.0; // resistance of R2 (10K) 

uint8_t power_1 = 0;
uint8_t power_2 = 0;
uint8_t power_3 = 0;
uint8_t power_4 = 0;
uint8_t power_5 = 0;

uint8_t U = 0; 

float sum_1 = 0;
float sum_2 = 0;
float sum_3 = 0;
float sum_4 = 0;
float sum_5 = 0;

ACS712 sensor_1(ACS712_05B, A1);
ACS712 sensor_2(ACS712_05B, A2);
ACS712 sensor_3(ACS712_05B, A3);
ACS712 sensor_4(ACS712_05B, A4);
ACS712 sensor_5(ACS712_05B, A5);

void setup() {
  

  pinMode(3, OUTPUT);//For PWM 
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);


  pinMode(A0, INPUT);//For sensors
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A4, INPUT);
  pinMode(A5, INPUT);

  pinMode(A6, INPUT); //Voltage
  
  Wire.begin(0xA1); 

  sensor_1.calibrate();
  sensor_2.calibrate();
  sensor_3.calibrate();
  sensor_4.calibrate();
  sensor_5.calibrate();

  Wire.onReceive(receiveEvent);
  Wire.onRequest(requestEvent);
}

void loop() {

      U = analogRead(A6);
      
      U = ((U * 5.0)/1024.0) / (R2/(R1+R2));
      
      if (U<0.09)
        U=0.0;

      
      
      if(U < 7){
        analogWrite(4, 0);
        analogWrite(5, 0);
        analogWrite(6, 0);
        analogWrite(9, 0);
        analogWrite(10, 0); 
      }else{
        analogWrite(4, 255*(power_1/100));
        analogWrite(5, 255*(power_1/100));
        analogWrite(6, 255*(power_1/100));
        analogWrite(9, 255*(power_1/100));
        analogWrite(10, 255*(power_1/100));   
      }

      

      float I_1 = sensor_1.getCurrentDC();
      float I_2 = sensor_2.getCurrentDC();
      float I_3 = sensor_3.getCurrentDC();
      float I_4 = sensor_4.getCurrentDC();
      float I_5 = sensor_5.getCurrentDC();
    
      sum_1 = U*I_1;
      sum_2 = U*I_2;
      sum_3 = U*I_3;
      sum_4 = U*I_4;
      sum_5 = U*I_5;

      if(0.05 > power_1){
        analogWrite(5, 0);
        analogWrite(6, 0);
        analogWrite(9, 0);
        analogWrite(10, 0);   
      }
      if(3 > power_2){
        analogWrite(6, 0);
        analogWrite(9, 0);
        analogWrite(10, 0);
      }
      if(0.4 > power_3){
        analogWrite(9, 0);
        analogWrite(10, 0);
      }
      if(18 > power_4){
        analogWrite(10, 0);
      }
      
      
//      voltage = U*1000;
      
}

void receiveEvent(int bytes) {
  if(bytes>1){
    power_1 = Wire.read();
    power_2 = Wire.read();
    power_3 = Wire.read();
    power_4 = Wire.read();
    power_5 = Wire.read();
  }
}

void requestEvent(){
  
//  Wire.write("1");
  Wire.write((uint8_t *)&sum_1, sizeof(&sum_1));//First
  
//  Wire.write("2");
  Wire.write((uint8_t *)&sum_2, sizeof(&sum_2));//Second
  
//  Wire.write("3");
  Wire.write((uint8_t *)&sum_3, sizeof(&sum_3));
  
//  Wire.write("4");
  Wire.write((uint8_t *)&sum_4, sizeof(&sum_4));

//  Wire.write("5");
  Wire.write((uint8_t *)&sum_5, sizeof(&sum_5));

  Wire.write((uint8_t *)&U, sizeof(U)); 

}
