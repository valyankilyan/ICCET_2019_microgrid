import random, time, threading, json

from Error import Error
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
from Consumer import Consumer

consumer = Consumer()
error = Error()

address = 8000

class Server(WebSocket):

    def handleMessage(self):
        
        # self.sendMessage(self.data)
        print "data = ", self.data
        try:
            dic = json.loads(self.data)
            print "json to dic = ", dic

        except:
            error.log("data sent isn't JSON")
            self.sendMessage("you sent not JSON")

        a = consumer.new_data(dic) 
        if a > 0:
            print "a > 0, send power to andrew ", a
            out = str(a)
            self.sendMessage(out)
        # except: 
        #     error.log("consumer doesn't work (main/handleMessage)")
    

    def handleConnected(self):
        print(self.address, 'connected')
        
    def handleClose(self):
        print(self.address, 'closed')

    def send(self, string):
        self.sendMessage(string)

    # def run():
    #     self.send(raw_input())
    # threading.Thread(target = run).start()


print "starting server"
serv = SimpleWebSocketServer('', address, Server)
serv.serveforever()
