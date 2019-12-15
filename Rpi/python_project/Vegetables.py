from Variables import Variables 
from I2C_data import Data
from Error import Error

error = Error()
var = Variables()
i2c = Data()

class Vegetables:
	def __init__(self):
		print "init Vegetables"

	def new_data(self, dic):
		print "Vegetables new data"
		
		try:
			var.vegetables_data[0] = dic["power"]
			var.vegetables_data[1] = dic["temperature"]
			var.vegetables_data[3] = dic["bright"]
			var.vegetables_data[4] = dic["red"]
			var.vegetables_data[5] = dic["green"]
			var.vegetables_data[6] = dic["blue"]
			var.vegetables_data[7] = dic["temperatue_now"]
		except:
			error.log("Vegetables rewrite data")

		i2c.write(var.vegetables_addr, var.vegetables_data[1:])