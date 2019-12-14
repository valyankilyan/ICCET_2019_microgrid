from Error import Error
from Data import Data
from Variables import Variables
import os

error = Error()
data = Data()
var = Variables()

class Scene():

	def __init__(self):
		print("init Scene")

	def change_music_id(self):
		print("Choise track")
		it = 1;
		for i in var.music_list:
			print it, "-", i
			it+= 1
		print("0 - exit")
		music_id =  input("Enter your choise: ")
		os.system('clear')
		if music_id == 0:
			return var.scene_data[0]
		if music_id >= len(var.music_list)+1:
			error.log("change music")
		else:
			return music_id

	def choise(self):
		print("choise Scene")
		while(True):
			print("Choise what do you want")
			print "1 - Change music, now playing", var.music_list[var.scene_data[0] - 1]
			print "2 - BASSBOOOST, now", var.scene_data[1]
			print("0 - exit")
			
			what = input("Enter your choise: ")
			os.system('clear')
			
			if what == 0:
				return
			
			if what == 1:
				var.scene_data[0] = self.change_music_id()
			
			if what == 2:
				print("choise bassboost")
				cin = input("Enter from 0 to 4: ")
				if cin <= 4 and cin >= 0:
					var.scene_data[1] = cin;
				else:
					what = 100
				os.system('clear')
			
			if what > 2 or what < 0:
				error.log("scene")
			else:
				data.write(var.ADDR_scene, var.scene_data)