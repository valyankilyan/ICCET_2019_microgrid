from Error import Error
from Data import Data
from Variables import Variables
from Change import Change
import os

error = Error()
data = Data()
var = Variables()
change = Change()

class Vegetables:
	
	def __init__(self):
		print("init Vegetables")

	def choise(self):
		while(True):
			print("choise Vegetables")
			print "Now there is ", var.vegetables_data[5], " C"
			print("Choise what do you want")
			print "1 - Change temperature ", var.vegetables_data[0], " C"
			print "2 - Change brightness ", var.vegetables_data[1], " %"
			print "3 - Change red light level ", var.vegetables_data[2], " %"
			print "4 - Change green light level ", var.vegetables_data[3], " %" 
			print "5 - Change blue light level ", var.vegetables_data[4], " %" 
			print("0 - exit")

			choise = input("Enter your choise: ")
			os.system('clear')
			
			if choise == 0:
				return

			if choise == 1:
				var.vegetables_data[0] = self.change_temperature()
			
			if choise >= 2 and choise <= 5:
				var.vegetables_data[choise - 1] = change.level(var.vegetables_data[choise - 1])
			
			if choise > 5 and choise < 0:
				error.log("vegetables")
			
			else:
				data.write(var.ADDR_vegetables, var.vegetables_data)

	def change_temperature(self):
		while(True):
			print("Choise temperature from 20 to 80 degrees of celsium")
			temp = input("Enter temperature: ")	
			os.system('clear')

			if temp <= 80 and temp >= 20:
				return temp
			else:
				error.log("change temerature")		
