from Error import Error
from Data import Data
from Variables import Variables
from Change import Change
import os

error = Error()
data = Data()
var = Variables()
change = Change()

class Radio:
	
	def __init__(self):
		print("init Radio")

	def choise(self):
		print("choise Radio")
		while(True):
			print("Choise what do you want")
			print "1 - ", ("On" if var.radio_data[0] else "Yes")
			print("0 - exit")

			choise = input("Enter your choise: ")
			os.system('clear')
			
			if choise == 0:
				return

			if choise == 1:
				var.radio_data[0] = (0 if var.radio_data[0] else 1)
				error.not_write()
			
			else:
				error.log("radio")
			
