#include "ACS712.h"
#include <Wire.h>
#include <StackArray.h>

#define CONS_COUNT 5 //КОЛИЧЕСТВО ПОТРЕБИТЕЛЕЙ
const int U = 9;
const int T = 50; // период измерения мощности

bool power[CONS_COUNT] = {0, 0, 0, 0, 0}, prosumer_power = 0;//включено устройство от даного источника или нет 
float pay[CONS_COUNT] = {0, 0, 0, 0, 0};//сколько натикало на каждом ватт секунд 
int controll_pin[CONS_COUNT] = {3, 5, 6, 9, 10}, last = -1;//пины на которых сидят транзисторы

long long int last_pay_time = 0;

ACS712 sensor_0(ACS712_05B, A1);
ACS712 sensor_1(ACS712_05B, A1);
ACS712 sensor_2(ACS712_05B, A2);
ACS712 sensor_3(ACS712_05B, A3);
ACS712 sensor_4(ACS712_05B, A6);

void setup() {
  for(int i = 0; i < CONS_COUNT; i++)
    pinMode(controll_pin[i], OUTPUT);

  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
  pinMode(A6, INPUT);
  
  Wire.begin(0x22);

  sensor_0.calibrate();
  sensor_1.calibrate();
  sensor_2.calibrate();
  sensor_3.calibrate();
  sensor_4.calibrate();

  Wire.onReceive(receiveEvent);
  Wire.onRequest(requestEvent);
}

void loop() {
      digitalWrite(11, prosumer_power);
      for(int i = 0; i < CONS_COUNT; i++)
        digitalWrite(controll_pin[i], power[i]);

      float I[CONS_COUNT] = {
        sensor_0.getCurrentDC(),
        sensor_1.getCurrentDC(),
        sensor_2.getCurrentDC(),
        sensor_3.getCurrentDC(),
        sensor_4.getCurrentDC()
      };

      if(millis() - last_pay_time > T)
        for(int i = 0; i < CONS_COUNT; i++)
          pay[last]+= U*I[i]*T/1000;  
}

void receiveEvent(int bytes) {
  if(bytes>1){
    int pw = Wire.read();
    for(int i = 0; i < CONS_COUNT; i++)
      power[i] = pw & (1<<i);
    prosumer_power = pw & (1<<CONS_COUNT);
    last = Wire.read();
  }
}

void requestEvent(){
  if(last != -1){
    Wire.write((uint8_t *)&pay[last], sizeof(&pay[last]));
    pay[last] = 0;
    last = -1;
  }
}
