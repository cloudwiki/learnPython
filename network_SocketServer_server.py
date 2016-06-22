#using socketserver module to simplify the coding on server
from SocketServer import TCPServer, StreamRequestHandler

class Handler(StreamRequestHandler): #request handler
    def handle(self):
        addr = self.request.getpeername()
        print 'Got connection from', addr
        self.wfile.write('Thank u for connecting')
        
server = TCPServer(('', 1234), Handler) #'' as the host name means that you're referring to the machine where the server is running.
server.serve_forever() #Each time the server gets a request (a connection from a client), a request handler is instantiated, and various handler methods are called on it to deal with the request
