from Error import Error
from Data import Data
from Variables import Variables
from Change import Change
import os

error = Error()
data = Data()
var = Variables()
change = Change()

class Light:
	
	def __init__(self):
		print("init Light")

	def choise(self):
		while(True):
			print("choise Light")
			print("Choise what do you want")
			print "1 - Change brightness ", var.light_data[0], " %"
			print "2 - Change red light level ", var.light_data[1], " %"
			print "3 - Change green light level ", var.light_data[2], " %" 
			print "4 - Change blue light level ", var.light_data[3], " %" 
			print "5 - Change mountain light brightness", var.light_data[4], " %"
			print("0 - exit")

			choise = input("Enter your choise: ")
			os.system('clear')
			
			if choise == 0:
				return

			if choise > 0 and choise < 6:
				var.light_data[choise - 1] = change.level(var.light_data[choise - 1])
			
			if choise > 5 and choise < 0:
				error.log("light")
			
			else:
				data.write(var.ADDR_light, var.light_data)
