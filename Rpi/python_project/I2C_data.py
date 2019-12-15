from smbus2 import SMBus, i2c_msg
import time
import os
import sys
from Error import Error

error = Error()

class Data:

	def __init__(self):
		print("init data")

	def write(self, addr, data):
		print "write i2c data " , addr, " ", data 
		try:
			with SMBus(1) as bus:
				try:
					msg = i2c_msg.write(addr, data)
					bus.i2c_rdwr(msg)	
					print "send data to " + addr + " " + data 
				
				except IOError as e:
					print "I/O error({0}): {1}".format(e.errno, e.strerror)
					time.sleep(1)
				
				except ValueError:
					print "Could not convert data to an integer."
					time.sleep(1)
				
				except:
					print "Unexpected error:", sys.exc_info()[0]
					time.sleep(1)
					raise
		except: 
			print "u have not i2c"

	def read(self, addr, data):
		print "read_byte"
		try:
			with SMBus(1) as bus:
				try:
					msg = i2c_msg.read(addr, len(data))
					read = bus.i2c_rdwr(msg)
					for i in msg:
						print int(i)
				except IOError as e:
					print "I/O error({0}): {1}".format(e.errno, e.strerror)
					time.sleep(1)
				
				except ValueError:
					print "Could not convert data to an integer."
					time.sleep(1)
				
				except:
					print "Unexpected error:", sys.exc_info()[0]
					time.sleep(1)
					raise
		except: 
			print "u have not i2c"