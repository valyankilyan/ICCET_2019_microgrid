from Error import Error
from Data import Data
from Variables import Variables
from Change import Change
import os

error = Error()
data = Data()
var = Variables()
change = Change()

class Wheel:
	
	def __init__(self):
		print("init Wheel")

	def choise(self):
		while(True):
			print("choise Wheel")
			print("Choise what do you want")
			print "1 - Change wheel speed ", var.wheel_data[0], " %"
			print("0 - exit")
			
			choise = input("Enter your choise: ")	
			os.system('clear')

			if choise == 0:
				return

			if choise == 1:
				var.wheel_data[0] = change.level(var.wheel_data[0])

			if choise > 2: 
				error.log("wheel")

			else:
				error.not_write()
				#data.write(var.ADDR_wheel, var.wheel_data)
