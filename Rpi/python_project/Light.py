from Variables import Variables 
from I2C_data import Data
from Error import Error

error = Error()
var = Variables()
i2c = Data()

class Light:
	def __init__(self):
		print "init Light"

	def new_data(self, dic):
		print "Light new data"
		
		try:
			var.light_data[0] = dic["power"]
			var.light_data[1] = dic["bright"]
			var.light_data[2] = dic["red"]
			var.light_data[3] = dic["green"]
			var.light_data[4] = dic["blue"]
			var.light_data[5] = dic["mountain"]
		except:
			error.log("Light rewrite data")
	
		i2c.write(var.light_addr, var.light_data[1:])