import os
from Error import Error
from Hydrate import Hydrate
from Battery import Battery
from Prosumer import Prosumer

error = Error()
hydrate = Hydrate()
battery = Battery()
prosumer = Prosumer()

class Generator:
	
	error = Error()
	
	def __init__(self):
		print("init generators")

	def choise(self):
		print("Generator choise")
		generators = {
		1 : "Hydrate generator",
		2 : "Battery",
		3 : "Prosumer"
		}

		while(True):
			print("Choise what do you want")
			for i in generators:
				print i, "-", generators[i]
			("0 - exit")
			choise = input("Enter your choise: ")
			os.system('clear')

			if choise == 0:
				return
			if choise == 1:
				hydrate.choise()
			if choise == 2:
				battery.choise()
			if choise == 3:
				prosumer.choise()
			if choise > 3 or choise < 0:
				error.log("generator")
			# else:
			# 	generators[choise].choise()				
