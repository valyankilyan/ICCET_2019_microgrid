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
		if dic["type"].lower() == "scene":
			print "it's Scene"
			scene.new_data(dic)

		elif dic["type"].lower() == "light":
			print "it's Light"
			light.new_data(dic)

		elif dic["type"].lower() == "radio":
			print "it's Radio"
			radio.new_data(dic)

		elif dic["type"].lower() == "smartgr":
			print "it's Vegetables"
			vegetables.new_data(dic)

		elif dic["type"].lower() == "wheel":
			print "it's Wheel"
			wheel.new_data(dic)

		else:
			error.log("JSON data: no such consumer " + dic["type"].lower())
