from Variables import Variables 
from I2C_data import Data
from Error import Error

error = Error()
var = Variables()
i2c = Data()

class Radio:
	def __init__(self):
		print "init Radio"

	def new_data(self, dic):
		print "Radio new data"
		
		try:
			var.scene_data[0] = dic["power"]
		except:
			error.log("Radio rewrite data")

		error.log("Didn't write code in radio")