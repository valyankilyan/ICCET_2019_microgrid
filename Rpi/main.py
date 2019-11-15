from smbus2 import SMBus, i2c_msg
from colorama import Fore
import time
import os

ADDR_1 = 16
ADDR_2 = 17
ADDR_3 = 18
ADDR_4 = 19
ADDR_5 = 20


def writeData(addr, data):
	with SMBus(1) as bus:
   		msg = i2c_msg.write(addr, data)
   		bus.i2c_rdwr(msg)	


def writeData_1():
	data = []

def writeData_2():
	data = []

def writeData_3():
	data = []

def writeData_4():
	data = []

def writeData_5():
	data = []


def prosumer_choise():
	print("Choise what do you want")
	print("1 - ")
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
		writeData_1()
	if what == 2:
		writeData_2()
	if what == 3:
		writeData_3()
	if what == 4:
		writeData_4()
	if what == 5:
		writeData_5()
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