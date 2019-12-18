from Variables import Variables 
from I2C_data import Data
from Error import Error
from Generator import Generator

generator = Generator()
error = Error()
var = Variables()
i2c = Data()

class Wheel:
	def __init__(self):
		print "init Wheel"

	def new_data(self, dic):
		print "Wheel new data"
	
		if dic.has_key("ask"):
			print "ask wheel out after dic.has_key(ask) in wheel/new_data"
			# try: 
			return generator.ask(dic)
			# except: 
			# 	print "wheel/new_data after generator ask"


		if dic.has_key("tariff") and dic.has_key("currentSupply"):
			var.wheel_data[0] = dic["tariff"]
			var.wheel_data[1] = dic["currentSupply"]
		else:
			error.log("Wheel/new data/ tariff or currentSupply (data hasn't key tariff, current and other")


		generator.reconf(dic)
		return -1