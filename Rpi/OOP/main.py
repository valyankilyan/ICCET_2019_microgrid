from smbus2 import SMBus, i2c_msg
import time
import os
from Consumer import Consumer
from Generator import Generator
from Error import Error
from Variables import Variables

consumer = Consumer()
generator = Generator()
error = Error()

while True:
	print("Choise what do you want")
	print("1 - consumers")
	print("2 - generators")
	what = input("Enter your choise: ")
	os.system('clear')
	if what == 1:
		consumer.choise()
	if what == 2:
		generator.choise()
	if what != 1 and what != 2:
		error.log("main menu")
