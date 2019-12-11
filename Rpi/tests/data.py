from smbus2 import SMBus, i2c_msg
import time
import os
import sys


def __init__():
	print("init data")

def write(addr, data):
	try:
		with SMBus(1) as bus:
			try:
				msg = i2c_msg.write(addr, data)
				bus.i2c_rdwr(msg)	
			
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

def read(addr):
	print "read"
	try:
		with SMBus(1) as bus:
			try:
			    write = i2c_msg.write(addr, [30, 100, 100, 100, 100, 25])
			    read = i2c_msg.read(addr, 2)				
			    bus.i2c_rdwr(write, read)
			    for i in read:
			    	print(read[i])				 

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

while(True):
	print "1 - write"
	print "2 - read"
	try:
		what = input()
	except:
		print "suck a cock"

	if what == 2:
		read(18)