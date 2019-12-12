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

def read_byte(addr):
	print "read_byte"
	try:
		with SMBus(1) as bus:
			try:
				b = bus.read_byte_data(addr, 0)
				print(b)
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

def read_block(addr):
	print "read_byte"
	try:
		with SMBus(1) as bus:
			try:
					# Read a block of 16 bytes from address 80, offset 0
				block = bus.read_i2c_block_data(addr, 0, 6)
					# Returned value is a list of 16 bytes
				print(block)

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
	print "2 - read one byte"
	print "3 - read block data"
	try:
		what = input()
	except:
		print "suck a cock"

	if what == 2:
		read_byte(18)
	if what == 3:
		read_block(18)