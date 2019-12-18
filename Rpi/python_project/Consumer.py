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
			return scene.new_data(dic)

		elif dic["type"].lower() == "light":
			print "it's Light"
			return light.new_data(dic)

		elif dic["type"].lower() == "radio":
			print "it's Radio"
			return radio.new_data(dic)

		elif dic["type"].lower() == "smartgr":
			print "it's Vegetables"
			return vegetables.new_data(dic)

		elif dic["type"].lower() == "wheel":
			print "it's Wheel"
			try:
				return wheel.new_data(dic)
			except: 
				print("wheel.new_data(dic) Consumer/new_data")

		else:
			error.log("JSON data: no such consumer " + dic["type"].lower())
