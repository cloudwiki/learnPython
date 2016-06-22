#using socket module
import socket
from time import sleep

s = socket.socket() #create a new socket object

host = socket.gethostname() #return current host name

port =1234

s.bind((host, port)) #Bind the socket to a local address

s.listen(5) # Enable a server to accept connections.  The backlog argument(5) must be at least 0
# it specifies the number of unaccepted connections that the system will allow before refusing new  connections.
# if connect request number exceed backlog, then socket.error: [Errno 10061] No connection could be made because the target machine actively refused it
while True:
    c, addr = s.accept() #accept a connection, returning new socket and client address
    print 'Got connection from', addr
    c.send('Thank u for connecting') #send data, may not send all of it
    sleep(20)
    c.close() #close the socket
