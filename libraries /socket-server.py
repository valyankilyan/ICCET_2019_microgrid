import threading
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import random, time


# from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

# clients = []
# class SimpleChat(WebSocket):

#     def handleMessage(self):
#        for client in clients:
#           if client != self:
#              client.sendMessage(self.address[0] + u' - ' + self.data)

#     def handleConnected(self):
#        print(self.address, 'connected')
#        for client in clients:
#           client.sendMessage(self.address[0] + u' - connected')
#        clients.append(self)

#     def handleClose(self):
#        clients.remove(self)
#        print(self.address, 'closed')
#        for client in clients:
#           client.sendMessage(self.address[0] + u' - disconnected')

# server = SimpleWebSocketServer('', 8000, SimpleChat)
# server.serveforever()



class SimpleEcho(WebSocket):

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



# def test_threading():
#     for i in range(100):
#         print i
#         SimpleEcho.send()
#         time.sleep(1)

# t = threading.Thread(target=test_threading)

server = SimpleWebSocketServer('', 8001, SimpleEcho)

# t.start()

server.serveforever()


# from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

# clients = []
# class SimpleChat(WebSocket):

#     def handleMessage(self):
#        for client in clients:
#           if client != self:
#              client.sendMessage(self.address[0] + u' - ' + self.data)

#     def handleConnected(self):
#        print(self.address, 'connected')
#        for client in clients:
#           client.sendMessage(self.address[0] + u' - connected')
#        clients.append(self)

#     def handleClose(self):
#        clients.remove(self)
#        print(self.address, 'closed')
#        for client in clients:
#           client.sendMessage(self.address[0] + u' - disconnected')

# server = SimpleWebSocketServer('', 8000, SimpleChat)
# server.serveforever()