import time

from colorama import Fore, Style

class Error:
	
	def __init__(self):
		print("init Error")

	def log(self, where):
		print(Fore.RED + "##ERROR " + Style.RESET_ALL + Fore.WHITE + where)	
		time.sleep(1)

	def not_write(self):
		print(Fore.RED + "##ERROR " + Style.RESET_ALL + Fore.WHITE + "u didn't write code for this")
		print "let's do this!!!!!!!!"			
		time.sleep(1)