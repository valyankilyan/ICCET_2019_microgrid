from Error import Error
from Data import Data
import os

error = Error()
data = Data()

ADDR_scene = 16
scene_data = [1, 0] #sound id, bassboost
music_list = ["Shrek theme", "From Vint", "Votting", "Soccer physics", "Dmitry", "John Sina", "SILENCE"]


class Scene:
	
	def __inint__(self):
		print("init Scene")

	def change_music_id(self):
		print("Choise track")
		it = 1;
		for i in music_list:
			print it, "-", i
			it+= 1
		print("0 - exit")
		music_id =  input("Enter your choise: ")
		os.system('clear')
		if music_id == 0:
			return scene_data[0]
		if music_id >= len(music_list)+1:
			error.log("change music")
		else:
			return music_id

	def choise(self):
		print("choise Scene")
		while(True):
			print("Choise what do you want")
			print "1 - Change music, now playing", music_list[scene_data[0] - 1]
			print "2 - BASSBOOOST, now", ("on" if scene_data[1] else "off") 
			print("0 - exit")
			
			what = input("Enter your choise: ")
			os.system('clear')
			
			if what == 0:
				return
			
			if what == 1:
				scene_data[0] = self.change_music_id()
			
			if what == 2:
				print("choise bassboost")
				cin = input("Enter from 0 to 4: ")
				if cin <= 4 and cin >= 0:
					scene_data[1] = cin;
				else:
					what = 100
				os.system('clear')
			
			if what > 2 or what < 0:
				error.log("scene")
			else:
				data.write(ADDR_scene, scene_data)