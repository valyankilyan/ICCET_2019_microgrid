import random, time, threading, os

from smbus2 import SMBus, i2c_msg
from Error import Error
from Variables import Variables

error = Error()
var = Variables()

while(True):
	print "it's working"
	time.sleep(10)
