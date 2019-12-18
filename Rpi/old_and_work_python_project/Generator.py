from Error import Error
from Variables import Variables
from HydroGen import HydroGen
from Battery import Battery
from Prosumer import Prosumer

error = Error()
var = Variables()
hydrogen = HydroGen()
battery = Battery()
prosumer = Prosumer()

class Generator:
	def __init__(self):
		print "init generators"	

	def reconfig(self, dic, gen):
		st = {
		"scene":0,
		"light":1,
		"radio":2,
		"smartgr":3, 
		"wheel":4
		}

		generators = ["hydrogen", "battery", "prosumer"]

		if gen == "battery":
			