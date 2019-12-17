import os, sys

from Error import Error

error = Error()

class Variables(object):
	scene_addr = 16
	scene_data = [1, 1, 0, 1] #sound id, bassboost, retry
	music_list = ["Shrek theme", "From Vint", "Soccer physics", "Dmitry", "John Sina", "SILENCE"]

	light_addr = 17
	light_data = [1, 100, 100, 100, 100]
	#current, 1, 2, 3, projector

	vegetables_addr = 18
	vegetables_data = [1, 30, 100, 100, 100, 100]
	#temperature, bright, red, green, blue, temperature now

	# radio and wheel have not address and set with generators
	radio_data = [1]#on or off
	wheel_data = [1, 100]#tariff on or off


	hydrogen_addr = 32
	hydrogen_power = [0]#consumers bit in bytes 0-sc, 1-lt, 2-veg, 3-rd, 4-wh; 
	hydrogen_pay = [0, 0, 0, 0, 0]
	# 	scene_power, light_power, radio_power, vegetables_power, wheel power;

	battery_addr = 33
	battery_power = [0] #test r, g, b
	battery_pay = [0, 0, 0, 0, 0]

	prosumer_addr = 34
	prosumer_power = [0] #test r, g, b
	prosumer_pay = [0, 0, 0, 0, 0]

	def __init__(self):
		print "init var"

	