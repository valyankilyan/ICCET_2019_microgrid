from smbus2 import SMBus, i2c_msg
from colorama import Fore
import time
import os

ADDR_scene = 16
scene_data = [1, 100] #sound id, sound level
music_list = ["Soccer physics soundtrack", "Sergey's trap", "Shrek theme"]

ADDR_light = 17
light_data = [100, 100, 100, 100]#bright, red, green, blue

ADDR_radio = 18
radio_data = [1]#on or off

ADDR_vegetables = 19
vegetables_data = [30, 100, 100, 100, 100]#temperature, bright, red, green, blue

ADDR_wheel = 20
wheel_data = [100, 100]#speed, bright


def writeData(addr, data):
	with SMBus(1) as bus:
   		msg = i2c_msg.write(addr, data)
   		bus.i2c_rdwr(msg)	


def change_scene_music_id():
	print("Choise track")
	it = 1;
	for i in music_list:
		print it, "-", i
		it+= 1
	music_id =  input("Enter your choise: ")
	os.system('clear')
	if music_id > 3:
		print(Fore.RED + "##ERROR" + Fore.WHITE + " No, sorry, we haven't")
	else:
		return music_id

def writeData_scene():
	print("Choise what do you want")
	print("1 - Change music")
	print("2 - Change music level")
	print("0 - exit")
	what = input("Enter your choise: ")
	os.system('clear')

	music_id = scene_data[0]
	soumd_level = scene_data[1]

	if what == 0:
		return
	if what == 1:
		music_id = change_scene_music_id()
	if what == 2:
		return
	if what > 2:
		print(Fore.RED + "##ERROR" + Fore.WHITE + " No, sorry, we haven't")
	else:
		scene_data[0] = music_id
		writeData(ADDR_scene, scene_data)



def writeData_light():
	data = []

def writeData_radio():
	data = []

def writeData_vegetables():
	data = []

def writeData_wheel():
	data = []


def prosumer_choise():
	print("Choise what do you want")
	print("1 - Scene")
	print("2 - ")
	print("3 - ")
	print("4 - ")
	print("5 - ")
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
		print(Fore.RED + "##ERROR" + Fore.WHITE + " No, sorry, we haven't")
		

def consumer_choise():
	print("Choise what do you want")
	print("1 - ")
	print("2 - ")
	print("3 - ")
	print("0 - exit")
	what = input("Enter your choise: ")
	os.system('clear')

	if what == 0:
		return
	if what == 1:
		writeData1()
	if what == 2:
		writeData2()
	if what == 3:
		writeData3()
	if what > 3:
		print(Fore.RED + "##ERROR" + Fore.WHITE + " No, sorry, we haven't")


while True:
	print("Choise what do you want")
	print("1 - prosumers")
	print("2 - consumers")
	what = input("Enter your choise: ")
	os.system('clear')
	if what == 1:
		prosumer_choise()
	if what == 2:
		consumer_choise()
	if what != 1 and what != 2:
		print(Fore.RED + "##ERROR" + Fore.WHITE + " No, sorry, we haven't")