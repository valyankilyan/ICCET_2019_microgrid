#include "ACS712.h"
#include <Wire.h>
#include <iarduino_I2C_connect.h>

const int 

uint8_t power_1 = 0;
uint8_t power_2 = 0;
uint8_t power_3 = 0;
uint8_t power_4 = 0;
uint8_t power_5 = 0;
uint8_t turn_prosumer = 0; //Включить/выкключить Prosumer;

struct Block{
  uint8_t hwo;
  uint8_t _for;
  //uint8_t _time;
  float sum;
}block_consumer1, block_consumer2, block_consumer3, block_consumer4, block_consumer5;

  ACS712 sensor_1(ACS712_30A, A0);
  ACS712 sensor_2(ACS712_30A, A1);
  ACS712 sensor_3(ACS712_30A, A2);
  ACS712 sensor_4(ACS712_30A, A3);
  ACS712 sensor_5(ACS712_30A, A6);// A4,A5 - I2C

void setup() {

  pinMode(3, OUTPUT);//For PWM 
  pinMode(5, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);


  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
  pinMode(A6, INPUT);

//  pinMode(A6, INPUT); // Напряжение
  
  Wire.begin(0x08);

  sensor_1.calibrate();
  sensor_2.calibrate();
  sensor_3.calibrate();
  sensor_4.calibrate();
  sensor_5.calibrate();
}

void loop() {
  unsigned long time = millis();
  for(int i = 0; i>-1; i++){
    
        if(time == 500*i){
          
            float I_1 = sensor_1.getCurrentAC();
            float I_2 = sensor_2.getCurrentAC();
            float I_3 = sensor_3.getCurrentAC();
            float I_4 = sensor_4.getCurrentAC();
            float I_5 = sensor_5.getCurrentAC();
          
            float U = analogRead(A6);
          
            //int time=millis();
          
            block_consumer1.sum = (U*I_1)*0.5;
            block_consumer2.sum = U*I_2*0.5;
            block_consumer3.sum = (U*I_3)*0.5;
            block_consumer4.sum = (U*I_4)*0.5;
            block_consumer5.sum = (U*I_5)*0.5;
          
            block_consumer1.hwo = 1;
            block_consumer2.hwo = 1;
            block_consumer3.hwo = 1;
            block_consumer4.hwo = 1;
            block_consumer5.hwo = 1;
          
            block_consumer1._for = 1;
            block_consumer2._for = 2;
            block_consumer3._for = 3;
            block_consumer4._for = 4;
            block_consumer5._for = 5;
          
            analogWrite(4, 255*(power_1/100));
            analogWrite(5, 255*(power_1/100));
            analogWrite(6, 255*(power_1/100));
            analogWrite(9, 255*(power_1/100));
            analogWrite(10, 255*(power_1/100));
            digitalWrite(3, turn_prosumer);
    }
  }
}

void receiveEvent(int bytes) {
  //чё-нибудь надо написать...
  if(bytes>1){
    power_1 = Wire.read();//In percents
    power_2 = Wire.read();
    power_3 = Wire.read();
    power_4 = Wire.read();
    power_5 = Wire.read();
    turn_prosumer = Wire.read();
    
  }
}

void requestEvent(){
  Wire.write((uint8_t *)&block_consumer1.hwo, sizeof(block_consumer1.hwo));//First
  Wire.write((uint8_t *)&block_consumer1._for, sizeof(block_consumer1._for));
  //Wire.write((uint8_t *)&block_consumer1._time, sizeof(block_consumer1._time));
  Wire.write((uint8_t *)&block_consumer1.sum, sizeof(block_consumer1.sum));

  Wire.write((uint8_t *)&block_consumer2.hwo, sizeof(block_consumer2.hwo));//First
  Wire.write((uint8_t *)&block_consumer2._for, sizeof(block_consumer2._for));
  //Wire.write((uint8_t *)&block_consumer2._time, sizeof(block_consumer2._time));
  Wire.write((uint8_t *)&block_consumer2.sum, sizeof(block_consumer2.sum));

  Wire.write((uint8_t *)&block_consumer3.hwo, sizeof(block_consumer3.hwo));//First
  Wire.write((uint8_t *)&block_consumer3._for, sizeof(block_consumer3._for));
  //Wire.write((uint8_t *)&block_consumer3._time, sizeof(block_consumer3._time));
  Wire.write((uint8_t *)&block_consumer3.sum, sizeof(block_consumer3.sum));

  Wire.write((uint8_t *)&block_consumer4.hwo, sizeof(block_consumer4.hwo));//First
  Wire.write((uint8_t *)&block_consumer4._for, sizeof(block_consumer4._for));
  //Wire.write((uint8_t *)&block_consumer4._time, sizeof(block_consumer4._time));
  Wire.write((uint8_t *)&block_consumer4.sum, sizeof(block_consumer4.sum));

  Wire.write((uint8_t *)&block_consumer5.hwo, sizeof(block_consumer5.hwo));//First
  Wire.write((uint8_t *)&block_consumer5._for, sizeof(block_consumer5._for));
  //Wire.write((uint8_t *)&block_consumer5._time, sizeof(block_consumer5._time));
  Wire.write((uint8_t *)&block_consumer5.sum, sizeof(block_consumer5.sum));
}
