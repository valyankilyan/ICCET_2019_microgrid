from Error import Error
from Variables import Variables
# from HydroGen import HydroGen
# from Battery import Battery
# from Prosumer import Prosumer
from I2C_data import Data

i2c = Data()
error = Error()
var = Variables()
# hydrogen = HydroGen()
# battery = Battery()
# prosumer = Prosumer()

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

		# if gen == "battery":


	def ask(self, dic):
		who = -1
		out = 1234
		try:
			who = 0 if dic["type"].lower() == "wheel" else who  
			who = 1 if dic["type"].lower() == "light" else who  
			who = 2 if dic["type"].lower() == "radio" else who  
			who = 3 if dic["type"].lower() == "smatgr" else who 
			who = 4 if dic["type"].lower() == "scene" else who  
			out = self.take_pay(who)
		except:
			error.log("in ask generator")
		print "generator/ask SEND ", out
		return out

	def take_pay(self, who):
		var.hydrogen_data[5] = who
		i2c.write(var.hydrogen_addr, var.hydrogen_data)
		pay = i2c.read(var.hydrogen_addr)

		var.battery_data[5] = who
		i2c.write(var.battery_addr, var.battery_data)
		pay += i2c.read(var.battery_addr)

		var.prosumer_data[5] = who
		i2c.write(var.prosumer_addr, var.prosumer_data)
		pay += i2c.read(var.prosumer_addr)

		out = 0
		for i in range(4):
			out += pay[3-i] * 2**i

		return out

	def reconf(self, dic):
		a = 0

			