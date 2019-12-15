from Variables import Variables 
from I2C_data import Data
from Error import Error

error = Error()
var = Variables()
i2c = Data()

class Scene:
	def __init__(self):
		print "init Scene"

	def new_data(self, dic):
		print "Scene new data"
		
		try:
			var.scene_data[0] = dic["currentSupply"]
			var.scene_data[1] = dic["track"]
			var.scene_data[2] = 1 if dic["bassboosted"] == True else 0 
			var.scene_data[3] = 1 if dic["retryTrack"] == True else 0 
		except:
			error.log("Scene rewrite data")
		
		print var.scene_data[1:]
		i2c.write(var.scene_addr, var.scene_data[1:])
