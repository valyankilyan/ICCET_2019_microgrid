from smbus2 import SMBus, i2c_msg
from colorama import Fore
import time
import os
import sys


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


	


def writeData(addr, data):
	with SMBus(1) as bus:
		try:
    		msg = i2c_msg.write(addr, data)
   			bus.i2c_rdwr(msg)	
		except IOError as e:
    		print "I/O error({0}): {1}".format(e.errno, e.strerror)
		except ValueError:
    		print "Could not convert data to an integer."
		except:
    		print "Unexpected error:", sys.exc_info()[0]
		    raise


def change_level(percent):
	print "Choise level from 0 to 100 %, now it's", percent, "%"
	out = input("Enter level: ")
	os.system('clear')

	if out <= 100 and out >= 0:
		return out
	else:
		print(Fore.RED + "##ERROR" + Fore.WHITE + " bad range")



def change_scene_music_id():
	print("Choise track")
	it = 1;
	for i in music_list:
		print it, "-", i
		it+= 1
	print("0 - exit")
	music_id =  input("Enter your choise: ")
	os.system('clear')
	if music_id == 0:
		return scene_data[0]
	if music_id >= len(music_list)+1:
		print(Fore.RED + "##ERROR" + Fore.WHITE + " we haven't this command")
	else:
		return music_id


def writeData_scene():
	while(True):
		print("Choise what do you want")
		print "1 - Change music, now playing", music_list[scene_data[0] - 1]
		print "2 - BASSBOOOST, now", ("on" if scene_data[1] else "off") 
		print("0 - exit")
		what = input("Enter your choise: ")
		os.system('clear')
		
		if what == 0:
			return
		if what == 1:
			scene_data[0] = change_scene_music_id()
		if what == 2:
			print("choise bassboost")
			cin = input("Enter from 0 to 4: ")
			if cin <= 4 and cin >= 0:
				scene_data[1] = cin;
			else:
				what = 100
			os.system('clear')
		if what > 2:
			print(Fore.RED + "##ERROR" + Fore.WHITE + " we haven't this command")
		else:
			writeData(ADDR_scene, scene_data)



def writeData_light():

	
#def writeData_radio():


def change_vegetables_temerature():
	print("Choise temperature from 20 to 80 degrees of celsium")
	temp = input("Enter temperature: ")	
	os.system('clear')
	if temp <= 80 and temp >= 20:
		return temp
	else:
		print(Fore.RED + "##ERROR" + Fore.WHITE + " bad range")

def writeData_vegetables():
	print("Choise what do you want")
	print "1 - Change temperature ", vegetables_data[0], "degrees of C"
	print "2 - Change brightness ", vegetables_data[1], " %"
	print "3 - Change red light level ", vegetables_data[2], " %"
	print "4 - Change green light level ", vegetables_data[3], " %" 
	print "5 - Change blue light level ", vegetables_data[4], " %" 
	print("0 - exit")
	what = input("Enter your choise: ")
	os.system('clear')
	if what == 1:
		vegetables_data[0] = change_vegetables_temerature()
	if what >= 2 and what <= 5:
		vegetables_data[what - 1] = change_level(vegetables_data[what - 1])
	if what > 5:
		print(Fore.RED + "##ERROR" + Fore.WHITE + " we haven't this command")
	else:
		writeData(ADDR_vegetables, vegetables_data)

	

def writeData_wheel():
	print("Choise what do you want")
	print "1 - Change wheel speed ", wheel_data[0], " %"
	print "2 - Change brightness ", wheel_data[1], " %"
	print("0 - exit")
	what = input("Enter your choise: ")	
	os.system('clear')
	if what == 0:
		return
	if what == 1:
		wheel_data[0] = change_level(wheel_data[0])
	if what == 2:
		wheel_data[1] = change_level(wheel_data[1])
	if what > 2: 
		print(Fore.RED + "##ERROR" + Fore.WHITE + " we haven't this command")
	else:
		writeData(ADDR_light, light_data)
	


def consumer_choise():
	print("Choise what do you want")
	print("1 - Scene")
	print("2 - Light")
	print("3 - Radio")
	print("4 - Vegetables")
	print("5 - Wheel")
	print("0 - exit")
	what = input("Enter your choise: ")
	os.system('clear')
	if what == 0:
		return
	if what == 1:
		writeData_scene()
	if what == 2:
		writeData_light()
	if what == 3:
		writeData_radio()
	if what == 4:
		writeData_vegetables()
	if what == 5:
		writeData_wheel()
	if what > 5:
		print(Fore.RED + "##ERROR" + Fore.WHITE + " we haven't this command")
		

def writeData_hydrate_generator():


def generator_choise():
	print("Choise what do you want")
	print("1 - hydrate generator")
	print("2 - ")
	print("3 - ")
	print("0 - exit")
	what = input("Enter your choise: ")
	os.system('clear')

	if what == 0:
		return
	if what == 1:
		writeData_hydrate_generator()
	if what == 2:
		writeData2()
	if what == 3:
		writeData3()
	if what > 3:
		print(Fore.RED + "##ERROR" + Fore.WHITE + " we haven't this command")


while True:
	print("Choise what do you want")
	print("1 - consumers")
	print("2 - generators")
	what = input("Enter your choise: ")
	os.system('clear')
	if what == 1:
		consumer_choise()
	if what == 2:
		generator_choise()
	if what != 1 and what != 2:
		print(Fore.RED + "##ERROR" + Fore.WHITE + " we haven't this command")