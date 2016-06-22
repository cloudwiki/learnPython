from SocketServer import TCPServer, ThreadingMixIn, StreamRequestHandler
from time import sleep

class Server(ThreadingMixIn, TCPServer): pass #using thread 

class Handler(StreamRequestHandler): #request handler
    def handle(self):
        addr = self.request.getpeername()
        print 'Got connection from', addr
        sleep(20)
        self.wfile.write('Thank u for connecting')
        
server = Server(('', 1234), Handler) #'' as the host name means that you're referring to the machine where the server is running.
server.serve_forever() #Each time the server gets a request (a connection from a client), a request handler is instantiated, and various handler methods are called on it to deal with the request
