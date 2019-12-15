import os
import sys
from Error import Error

error = Error()

class Variables(object):
	ADDR_scene = 16
	scene_data = [1, 0, 1] #sound id, bassboost
	music_list = ["Shrek theme", "From Vint", "Soccer physics", "Dmitry", "John Sina", "SILENCE"]

	ADDR_light = 17
	light_data = [100, 100, 100, 100, 100]#bright, red, green, blue, mountain

	ADDR_vegetables = 18
	vegetables_data = [30, 100, 100, 100, 100, 25]#temperature, bright, red, green, blue, temperature now

	# radio and wheel have not address and set with generators
	radio_data = [1]#on or off
	wheel_data = [100]#speed and light in %


	ADDR_h_gen = 32
	data_h_gen = [1+2+4+8+16, 0, 0, 0, 0, 0]#consumers bit in bytes 0-sc, 1-lt, 2-veg, 3-rd, 4-wh; 
	# 	scene_power, light_power, radio_power, vegetables_power, wheel power;

	ADDR_battery = 33
	data_battery = [100, 100, 100] #test r, g, b

	def __init__(self):
		print "init var"

	