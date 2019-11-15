from smbus2 import SMBus, i2c_msg
import time

address = 16

count = input("Enter count of data: ")

data = []
for i in range(count):
	data.append(input("Write byte: "))
  	
with SMBus(1) as bus:
   	msg = i2c_msg.write(address, data)
   	bus.i2c_rdwr(msg)	
   
time.sleep(2)