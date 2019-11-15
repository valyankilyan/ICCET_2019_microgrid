from smbus2 import SMBus, i2c_msg
import time


# This is the address we setup in the Arduino Program
address = 16

# def writeNumber(data):
# 	with SMBus(1) as bus:
# 		msg = i2c_msg.write(address, data)
#     	bus.i2c_rdwr(msg)	
	# 	msg = i2c_msg.write(address, [1, 2, 3, 4, 5])
 #    	bus.i2c_rdwr(msg)
# bus.write_byte_data(address, 0, value)
	# return -1

# def readNumber():
# 	with SMBus(1) as bus:
# 		msg = i2c_msg.write(address, data)
#     	bus.i2c_rdwr(msg)
# 		number = bus.read_byte(address)
# # number = bus.read_byte_data(address, 1)
# 		return number

while True:
	count = input("Enter count of data: ")
	if not count:
		continue

	# data = [146, 56, 53, 44, 55, 67, 79, 48, 210]

	# for i in range(count):
	# 	data.append(input("Write byte: "))

	with SMBus(1) as bus:
		msg = i2c_msg.write(address, [10, 20, 60, 68])
    	bus.i2c_rdwr(msg)	
		# msg = i2c_msg.write(address, [146, 56, 53, 44, 55, 67, 79, 48, 210])
  #   	bus.i2c_rdwr(msg)	

	#writeNumber(data)
# sleep one second
	time.sleep(1)
	# number = readNumber()
	# print(chr(number))
