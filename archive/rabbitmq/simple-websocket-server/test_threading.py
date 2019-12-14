import threading, time

def func1():
	for i in range(10):
		print(1)
		time.sleep(1)

def func2():
	for i in range(6):
		print(2)
		time.sleep(2)

t1 = threading.Thread(target = func1)
t2 = threading.Thread(target = func2)

t1.start()
t2.start()