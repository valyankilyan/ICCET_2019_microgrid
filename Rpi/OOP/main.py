from smbus2 import SMBus, i2c_msg
import time
import os
from Consumer import Consumer
from Generator import Generator
from Error import Error

consumer = Consumer()
generator = Generator()
error = Error()

ADDR_scene = 16
scene_data = [1, 0] #sound id, bassboost
music_list = ["Shrek theme", "From Vint", "Votting", "Soccer physics", "Dmitry", "John Sina", "SILENCE"]

ADDR_light = 17
light_data = [100, 100, 100, 100]#bright, red, green, blue

ADDR_vegetables = 18
vegetables_data = [30, 100, 100, 100, 100]#temperature, bright, red, green, blue

# radio and wheel have not address and set with generators
radio_data = [1]#on or off
wheel_data = [100, 100]#speed and light in %


ADDR_h_gen = 32
ADDR_h_gen = [1+2+4+8+16, 0, 0, 0, 0, 0]#consumers bit in bytes 0-sc, 1-lt, 2-veg, 3-rd, 4-wh; 
# 	scene_power, light_power, radio_power, vegetables_power, wheel power;


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
