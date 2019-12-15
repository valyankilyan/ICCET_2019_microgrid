import random, time, threading, json

from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
from Consumer import Consumer

consumer = Consumer()

address = 8000

class Server(WebSocket):

    def handleMessage(self):
        
        self.sendMessage(self.data)
        print(self.data)

        dic = json.loads(self.data)
        consumer.new_data(dic)
    

    def handleConnected(self):
        print(self.address, 'connected')
        
    def handleClose(self):
        print(self.address, 'closed')

    def send(self, string):
        self.sendMessage(string)


print "starting server"
serv = SimpleWebSocketServer('', address, Server)
serv.serveforever()
