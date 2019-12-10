from Error import Error
import os

error = Error()

class Change:
	
	def __init__(self):
		print("init change")

	def level(self, percent):
		while(True):
			print "Choise level from 0 to 100 %, now it's", percent, "%"
			out = input("Enter level: ")
			os.system('clear')

			if out <= 100 and out >= 0:
				return out
			else:
				error.log("change level")