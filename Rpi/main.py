import smbus
import time
# for RPI version 1, use “bus = smbus.SMBus(0)”
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x10

def writeNumber(value):
	bus.write_byte(address, value)
# bus.write_byte_data(address, 0, value)
	return -1

def readNumber():
	number = bus.read_byte(address)
# number = bus.read_byte_data(address, 1)
	return number

while True:
	var = input("Enter: ")
	if not var:
		continue

	writeNumber(var)
# sleep one second
	time.sleep(1)
	number = readNumber()
	