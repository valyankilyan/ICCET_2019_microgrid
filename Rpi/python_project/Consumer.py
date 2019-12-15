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
			scene.new_data(dic)

		elif dic[0] == "Light":
			print "it's Light"
			light.new_data(dic)

		elif dic[0] == "Radio":
			print "it's Radio"
			radio.new_data(dic)

		elif dic[0] == "Vegetables":
			print "it's Vegetables"
			vegetables.new_data(dic)

		elif dic[0] == "Wheel":
			print "it's Wheel"
			wheel.new_data(dic)

		else:
			error.log("JSON data: no such consumer " + dic[0])
