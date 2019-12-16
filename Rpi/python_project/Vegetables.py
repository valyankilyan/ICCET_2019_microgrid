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
			var.vegetables_data[0] = dic["currentSupply"]
			var.vegetables_data[1] = dic["temperature"]
			var.vegetables_data[3] = dic["lightLevel"]
			var.vegetables_data[4] = dic["redlevel"]
			var.vegetables_data[5] = dic["greenlevel"]
			var.vegetables_data[6] = dic["bluelevel"]
		except:
			error.log("Vegetables rewrite data")

		i2c.write(var.vegetables_addr, var.vegetables_data[1:])
{"type":"SmartGR","lightLevel":22,"redLevel":16,"greenLevel":15,"blueLevel":16,"temperature":23,"currentSupply":true,"tariff":false}
