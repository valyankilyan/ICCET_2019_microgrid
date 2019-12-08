from smbus2 import SMBus, i2c_msg
import os
import sys
from Error import Error

error = Error()

class Data:

	def __init__(self):
		print("init data")

	def write(self, addr, data):
		with SMBus(1) as bus:
			try:
				msg = i2c_msg.write(addr, data)
	   			bus.i2c_rdwr(msg)	
			
			except IOError as e:
				print "I/O error({0}): {1}".format(e.errno, e.strerror)
			
			except ValueError:
				print "Could not convert data to an integer."
			
			except:
				print "Unexpected error:", sys.exc_info()[0]
				raise

	def read(self):

