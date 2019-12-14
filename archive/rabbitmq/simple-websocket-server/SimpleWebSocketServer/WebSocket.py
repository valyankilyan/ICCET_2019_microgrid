import threading
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import random, time


class SocketServer(WebSocket):

	def handleMessage(self):
		# echo message back to client
		self.sendMessage(self.data)
		print(self.data)

		def run():
			self.send("poshel naher kozel")
			for i in range(3):
				time.sleep(1)
				self.send(str(i*135))
				time.sleep(1)
			print("thread terminating...")
			if self.data == 'scene':
				threading.Thread(target=run).start()

	def handleConnected(self):
		print(self.address, 'connected')

	def handleClose(self):
		print(self.address, 'closed')

	def send(self, string):
		self.sendMessage(string)


server = SimpleWebSocketServer('', 8001, SimpleEcho)
server.serveforever()
