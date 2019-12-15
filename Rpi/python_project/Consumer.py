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

	def new_data(self, dic):
		if dic[0] == "Scene":
			print "it's Scene"

		elif dic[0] == "Light":
			print "it's Light"

		elif dic[0] == "Radio":
			print "it's Radio"

		elif dic[0] == "Vegetables":
			print "it's Vegetables"

		elif dic[0] == "Wheel":
			print "it's Wheel"

		else:
			error.log("JSON data: no such consumer " + dic[0])
