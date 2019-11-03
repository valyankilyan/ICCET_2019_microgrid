#include <Wire.h>

#define SLAVE_ADDRESS 0x10
int out = -1;

void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600); // start serial for output
  // initialize i2c as slave
  Wire.begin(SLAVE_ADDRESS);
  
  // define callbacks for i2c communication
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
  
  Serial.println("Ready!");
}

void loop() {
  int a = Serial.read();
  if(a!= -1 && a != 10){
    out = a;
    Serial.print("we make out = ");
    Serial.println(out);
  }
}

// callback for received data
void receiveData(int byteCount){
  while(Wire.available()) {
    Serial.print("data received: ");
    Serial.println(Wire.read());
  }
}

// callback for sending data
void sendData(){
  if(out != -1){
    Wire.write(out);
    Serial.print("We sent ");
    Serial.println(out);
  }
}
