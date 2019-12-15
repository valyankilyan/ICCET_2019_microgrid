import random, time, threading, os

from smbus2 import SMBus, i2c_msg
from Error import Error
from Variables import Variables
from Consumer import Consumer

consumer = Consumer()
error = Error()
var = Variables()

while(True):
	print "it's working"
	time.sleep(10)
