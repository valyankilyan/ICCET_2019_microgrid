import os
from Error import Error
from Scene import Scene 
from Light import Light
from Radio import Radio
from Vegetables import Vegetables
from Wheel import Wheel

error = Error()
scene = Scene()
light = Light()
radio = Radio()
vegetables = Vegetables()
wheel = Wheel()

class Consumer:

	def __init__(self):
		print("init consumers")

	def choise(self):
		consumers = {
		1 : "Scene",
		2 : "Light",
		3 : "Radio",
		4 : "Vegetables",
		5 : "Wheel"
		}

		while(True):
			print("Choise what do you want")
			for i in consumers:
				print i, "-", consumers[i]
			("0 - exit")
			choise = input("Enter your choise: ")
			os.system('clear')

			if choise == 0:
				return
			if choise == 1:
				scene.choise()
			if choise == 2:
				light.choise()
			if choise == 3:
				radio.choise()
			if choise == 4:
				vegetables.choise()
			if choise == 5:
				wheel.choise()	
			if choise > 5 or choise < 0:
				error.log("consumer")
			# else:
			# 	consumers[choise].choise()				

	def write_scene():
		print("write_scene")
