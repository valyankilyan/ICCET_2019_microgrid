import random, time, threading, json

from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

class Server(WebSocket):

    def handleMessage(self):
        
        self.sendMessage(self.data)
        print(self.data)

        def run():
            dic = json.loads(self.data)
            for i in dic:
                print i, dic[i]    
        
        threading.Thread(target=run).start()

    def handleConnected(self):
        print(self.address, 'connected')
        
    def handleClose(self):
        print(self.address, 'closed')

    def send(self, string):
        self.sendMessage(string)


print "starting server"
serv = SimpleWebSocketServer('', 1234, Server)
serv.serveforever()
