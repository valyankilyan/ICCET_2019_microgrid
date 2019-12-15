from Variables import Variables 
from I2C_data import Data
from Error import Error

error = Error()
var = Variables()
i2c = Data()

class Wheel:
	def __init__(self):
		print "init Wheel"

	def new_data(self, dic):
		print "Wheel new data"
		
		try:
			var.wheel_data[0] = dic["tariff"]
			var.wheel_data[1] = dic["currentSupply"]
		except:
			error.log("Wheel rewrite data")

		i2c.write(var.wheel_addr, var.wheel_data[1:])