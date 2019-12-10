from Error import Error
from Data import Data
from Variables import Variables
from Change import Change
import os

error = Error()
data = Data()
var = Variables()
change = Change()

class Battery:
	
	def __init__(self):
		print("init Battery")

	def choise(self):
		print("choise Battery")
		print("test choise light level")
		print("1 - red")
		print("2 - green")
		print("3 - blue")
		print("0 - exit")
		
		what = input("Enter your choise: ")
		os.system('clear')
		
		if what == 0:
			return
		
		if what < 0 or what > 3:
			error.log("battery choise")
		else:	
			var.data_battery[what-1] = change.level(var.data_battery[what-1])
			data.write(var.ADDR_battery, var.data_battery)