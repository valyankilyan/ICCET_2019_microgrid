from colorama import Fore, Style

class Error:
	
	def __init__(self):
		print("init Error")

	def log(self, where):
		print(Fore.RED + "##ERROR " + Style.RESET_ALL + Fore.WHITE + where)	