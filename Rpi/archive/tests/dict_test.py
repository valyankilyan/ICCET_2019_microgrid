import random, time, threading, json

class test:
	def __init__(self):
		print "init"
	def t(self, a):
		print a
	def Scene(self, a):
		print a

js = '{"type":"Scene","WHswitch2":false}'

dic = json.loads(js)
print dic
print dic["type"]
tt = test()
tt.dic["type"]("it's working")