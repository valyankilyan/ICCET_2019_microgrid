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
			var.light_data[0] = dic["current Suply"]
			var.light_data[1] = dic["house1"]
			var.light_data[2] = dic["house2"]
			var.light_data[3] = dic["house3"]
			var.light_data[4] = 1 if dic["projector"] == True else 0
		except:
			error.log("Light rewrite data")
	
		i2c.write(var.light_addr, var.light_data[1:])