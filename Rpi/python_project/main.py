import random, time, threading, json

from Error import Error
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
from Consumer import Consumer

consumer = Consumer()
error = Error()

address = 8000

class Server(WebSocket):

    def handleMessage(self):
        
        self.sendMessage(self.data)
        print(self.data)
        try:
            dic = json.loads(self.data)
            print dic
        except:
            error.log("data sent isn't JSON")
            self.sendMessage("you sent not JSON")

        # try:
        consumer.new_data(dic)
        # except: 
        #     error.log("consumer doesn't work")
    

    def handleConnected(self):
        print(self.address, 'connected')
        
    def handleClose(self):
        print(self.address, 'closed')

    def send(self, string):
        self.sendMessage(string)


print "starting server"
serv = SimpleWebSocketServer('', address, Server)
serv.serveforever()
